"""Application credentials platform for Heiman."""

import asyncio
import logging
from json import JSONDecodeError
from typing import NoReturn, cast

from aiohttp import BasicAuth, ClientError, ClientResponse, RequestInfo
from homeassistant.components.application_credentials import (
    AuthImplementation,
    AuthorizationServer,
    ClientCredential,
)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import (
    OAuth2TokenRequestError,
    OAuth2TokenRequestReauthError,
    OAuth2TokenRequestTransientError,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from yarl import URL

from .const import OAUTH_AUTHORIZE_URL, OAUTH_TOKEN_URL

_LOGGER = logging.getLogger(__name__)

# Default OAuth credentials for Heiman Home
DEFAULT_CLIENT_ID = "htJXYn5TyM3zZ7ji"
DEFAULT_CLIENT_SECRET = "htJXYn5TyM3zZ7ji"


async def async_get_auth_implementation(
    hass: HomeAssistant, auth_domain: str, credential: ClientCredential
) -> AuthImplementation:
    """Return auth implementation.

    If no credentials are provided, use default credentials for Heiman Home.
    """
    # Use provided credentials or fall back to defaults
    client_id = credential.client_id if credential.client_id else DEFAULT_CLIENT_ID
    client_secret = (
        credential.client_secret if credential.client_secret else DEFAULT_CLIENT_SECRET
    )

    return HeimanOAuth2Implementation(
        hass,
        auth_domain,
        ClientCredential(client_id=client_id, client_secret=client_secret),
        authorization_server=AuthorizationServer(
            authorize_url=OAUTH_AUTHORIZE_URL,
            token_url=OAUTH_TOKEN_URL,
        ),
    )


class HeimanOAuth2Implementation(AuthImplementation):
    """Heiman-specific OAuth2 implementation.

    This specialization is needed because Heiman's OAuth2 token endpoint
    requires custom error handling and response validation that differs
    from the standard OAuth2 flow. Specifically:
    - Custom error code mapping for re-authentication scenarios
    - Special handling for empty responses (expired refresh tokens)
    - Detailed logging for debugging token issues
    """

    async def _token_request(self, data: dict) -> dict:
        """Make a token request."""
        session = async_get_clientsession(self.hass)

        # --- Retry the HTTP POST on transient network errors ---
        max_retries = 3
        resp = None
        for attempt in range(max_retries):
            try:
                resp = await session.post(
                    self.token_url,
                    data=data,
                    auth=BasicAuth(self.client_id, self.client_secret),
                )
                break  # POST succeeded, exit retry loop
            except TimeoutError as err:
                if attempt < max_retries - 1:
                    delay = 2**attempt
                    _LOGGER.warning(
                        "Token request timeout (attempt %d/%d), retrying in %ds: %s",
                        attempt + 1,
                        max_retries,
                        delay,
                        err,
                    )
                    await asyncio.sleep(delay)
                else:
                    _LOGGER.error(
                        "Token request timed out after %d attempts", max_retries
                    )
                    request_info = RequestInfo(
                        url=URL(self.token_url),
                        method="POST",
                        headers={},  # type: ignore[arg-type]
                        real_url=URL(self.token_url),
                    )
                    raise OAuth2TokenRequestTransientError(
                        request_info=request_info,
                        history=(),
                        status=0,
                        headers=None,
                        domain=self.domain,
                    ) from err
            except OSError as err:
                if attempt < max_retries - 1:
                    delay = 2**attempt
                    _LOGGER.warning(
                        "Token request network error (attempt %d/%d), "
                        "retrying in %ds: %s",
                        attempt + 1,
                        max_retries,
                        delay,
                        err,
                    )
                    await asyncio.sleep(delay)
                else:
                    _LOGGER.error(
                        "Token request failed after %d attempts "
                        "due to network error: %s",
                        max_retries,
                        err,
                    )
                    request_info = RequestInfo(
                        url=URL(self.token_url),
                        method="POST",
                        headers={},  # type: ignore[arg-type]
                        real_url=URL(self.token_url),
                    )
                    raise OAuth2TokenRequestTransientError(
                        request_info=request_info,
                        history=(),
                        status=0,
                        headers=None,
                        domain=self.domain,
                    ) from err
            except ClientError as err:
                # ClientError subclasses that represent protocol-level
                # failures (not network-level) are NOT retried.
                _LOGGER.error("Token request for %s failed: %s", self.domain, err)
                request_info = getattr(err, "request_info", None)
                if request_info is None:
                    request_info = RequestInfo(
                        url=URL(self.token_url),
                        method="POST",
                        headers={},  # type: ignore[arg-type]
                        real_url=URL(self.token_url),
                    )
                raise OAuth2TokenRequestTransientError(
                    request_info=request_info,
                    history=getattr(err, "history", ()),
                    status=getattr(err, "status", 0),
                    headers=getattr(err, "headers", None),
                    domain=self.domain,
                ) from err

        # At this point resp is guaranteed to be set
        result: dict | None = None
        try:
            # Check for error status codes
            if resp.status >= 400:
                try:
                    error_response = await resp.json()
                except (ClientError, JSONDecodeError):
                    error_response = {}
                error_code = error_response.get("error", "unknown")
                error_description = error_response.get(
                    "error_description", "unknown error"
                )
                _LOGGER.error(
                    "Token request for %s failed (%s): %s",
                    self.domain,
                    error_code,
                    error_description,
                )

                self._raise_token_error(resp, error_code)

            # Try to parse JSON response
            try:
                result = await self._parse_token_response(resp)
            except OAuth2TokenRequestError:
                raise
            except (ValueError, ClientError, JSONDecodeError) as err:
                _LOGGER.exception("Failed to process token response")
                self._raise_token_error(resp, from_exception=err)
            else:
                if result is None:  # pragma: no cover
                    msg = "Unexpected: _token_request completed without returning"
                    raise AssertionError(msg)

                return result

        except OAuth2TokenRequestError:
            raise
        finally:
            if resp is not None:
                resp.release()

    def _raise_token_error(
        self,
        resp: ClientResponse,
        error_code: str | None = None,
        from_exception: Exception | None = None,
    ) -> NoReturn:
        """Raise appropriate OAuth2 token request error.

        Args:
            resp: HTTP response object
            error_code: Error code from response body (optional)
            from_exception: Original exception to chain from (optional)

        Raises:
            OAuth2TokenRequestReauthError: For authentication errors
                that require the user to re-authorize.
            OAuth2TokenRequestTransientError: For temporary errors
                that may succeed on retry.
            OAuth2TokenRequestError: For other errors.
        """
        # ---- Re-authentication errors ----
        # These errors mean the credentials are permanently invalid and
        # the user must go through the OAuth2 flow again.
        _REAUTH_CODES: frozenset[str] = frozenset(
            {
                "invalid_grant",
                "invalid_token",
                "unauthorized_client",
                "invalid_client",
                "access_denied",
                "unsupported_grant_type",
            }
        )
        if error_code and error_code in _REAUTH_CODES:
            raise OAuth2TokenRequestReauthError(
                request_info=resp.request_info,
                history=resp.history,
                status=resp.status,
                headers=resp.headers,
                domain=self.domain,
            )

        # 401 Unauthorized without a recognized error_code also
        # indicates a credential problem -> re-auth.
        if resp.status == 401:
            raise OAuth2TokenRequestReauthError(
                request_info=resp.request_info,
                history=resp.history,
                status=resp.status,
                headers=resp.headers,
                domain=self.domain,
            )

        # ---- Transient / retryable errors ----
        # Server errors (5xx) and rate-limiting (429) are temporary.
        if resp.status >= 500 or resp.status == 429:
            raise OAuth2TokenRequestTransientError(
                request_info=resp.request_info,
                history=resp.history,
                status=resp.status,
                headers=resp.headers,
                domain=self.domain,
            )

        # ---- General error fallback ----
        raise OAuth2TokenRequestError(
            request_info=resp.request_info,
            history=resp.history,
            status=resp.status,
            headers=resp.headers,
            domain=self.domain,
        ) from from_exception

    async def _parse_token_response(self, resp: ClientResponse) -> dict:
        """Parse and validate token response.

        Args:
            resp: HTTP response object

        Returns:
            Parsed response data as dictionary

        Raises:
            ValueError: If response is empty or invalid
        """
        # First check if response has content
        text = await resp.text()

        if not text or not text.strip():
            _LOGGER.error(
                "Token request returned empty response (status %s). "
                "This may indicate an invalid refresh token or expired credentials",
                resp.status,
            )
            msg = f"Empty response from token endpoint (status {resp.status})"
            raise ValueError(msg)

        # Try to parse as JSON
        try:
            response_data = await resp.json()
            return cast(dict, response_data)
        except (ClientError, JSONDecodeError):
            _LOGGER.exception(
                "Token request returned non-JSON response (status %s, content_type='%s'): %s",
                resp.status,
                resp.content_type,
                text[:500] if text else "(empty)",
            )
            raise
