"""Config flow to configure Heiman."""

from collections.abc import Mapping
import logging
from typing import Any

import voluptuous as vol

from homeassistant.components.application_credentials import (
    ClientCredential,
    async_import_client_credential,
)
from homeassistant.config_entries import SOURCE_REAUTH, ConfigFlowResult
from homeassistant.const import CONF_TOKEN
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler

from .api import HeimanApiClient, HeimanHome
from .const import CONF_HOME_ID, CONF_USER_ID, DOMAIN

_LOGGER = logging.getLogger(__name__)

# Default OAuth credentials for Heiman Home
DEFAULT_CLIENT_ID = "htJXYn5TyM3zZ7ji"
DEFAULT_CLIENT_SECRET = "htJXYn5TyM3zZ7ji"


class AuthInfo:
    """Store authentication info temporarily during config flow."""

    def __init__(self) -> None:
        """Initialize auth info."""
        self.homes: list[HeimanHome] = []
        self.user_info: Any = None
        self.auth_data: dict[str, Any] = {}


class HeimanConfigFlow(AbstractOAuth2FlowHandler, domain=DOMAIN):
    """Handle configuration of Heiman integration."""

    VERSION = 1
    MINOR_VERSION = 1
    DOMAIN = DOMAIN

    def __init__(self) -> None:
        """Initialize the config flow."""
        super().__init__()
        self._auth_info = AuthInfo()
        # Ensure default credentials are registered
        self._credentials_registered = False

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)

    @property
    def extra_authorize_data(self) -> dict[str, Any]:
        """Extra data that needs to be appended to the authorize url."""
        return {}

    async def async_step_pick_implementation(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Skip implementation selection and use default.
        
        This automatically uses the registered OAuth credentials without
        showing the selection form to the user.
        """
        # Register default credentials if not already done
        if not self._credentials_registered:
            try:
                await async_import_client_credential(
                    self.hass,
                    DOMAIN,
                    ClientCredential(
                        client_id=DEFAULT_CLIENT_ID,
                        client_secret=DEFAULT_CLIENT_SECRET,
                    ),
                )
                _LOGGER.info("Default OAuth credentials registered successfully")
                self._credentials_registered = True
            except Exception as err:  # noqa: BLE001
                _LOGGER.warning("Failed to register default credentials: %s", err)
        
        # Call parent method with user_input to trigger auto-selection
        # The parent class already handles single implementation case
        return await super().async_step_pick_implementation(user_input)

    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult:
        """Create an entry for Heiman."""
        # Create API client to validate token and get user info
        api_client = HeimanApiClient(
            hass=self.hass, session=None, token_data=data[CONF_TOKEN]
        )

        try:
            user_info = await api_client.async_get_user_info()
        except ConfigEntryAuthFailed:
            return self.async_abort(reason="token_invalid")
        except Exception as err:  # noqa: BLE001
            _LOGGER.error("Failed to get user info: %s", err)
            return self.async_abort(reason="user_info_failed")

        # Get home info
        try:
            homes = await api_client.async_get_homes()
            if not homes:
                return self.async_abort(reason="no_homes")
        except ConfigEntryAuthFailed:
            return self.async_abort(reason="token_invalid")
        except Exception as err:  # noqa: BLE001
            _LOGGER.error("Failed to get homes: %s", err)
            return self.async_abort(reason="homes_fetch_failed")
        finally:
            # Ensure the API client is always closed to avoid leaking resources
            await api_client.close()

        # Store temporary data for home selection
        self._auth_info.homes = homes if isinstance(homes, list) else []
        self._auth_info.user_info = user_info
        self._auth_info.auth_data = data

        # Enter home selection step
        return await self.async_step_select_home()

    async def async_step_select_home(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle home selection step."""
        if user_input is not None:
            # User selected a home
            selected_home_id = user_input.get(CONF_HOME_ID)

            if not selected_home_id:
                return self.async_show_form(
                    step_id="select_home",
                    data_schema=self._get_home_selection_schema(),
                    errors={"base": "no_home_selected"},
                )

            # Use home_id as unique_id to allow multiple homes per user
            await self.async_set_unique_id(f"{self._auth_info.user_info.user_id}_{selected_home_id}")

            if self.source != SOURCE_REAUTH:
                self._abort_if_unique_id_configured()

                # Build config data with single home ID
                config_data = {
                    **self._auth_info.auth_data,
                    CONF_HOME_ID: selected_home_id,
                    CONF_USER_ID: self._auth_info.user_info.user_id,
                }

                # Get title from home name and user info
                selected_home = next(
                    (h for h in self._auth_info.homes if h.home_id == selected_home_id),
                    None,
                )
                home_name = getattr(selected_home, "home_name", "Home") if selected_home else "Home"
                user_info = self._auth_info.user_info
                user_name = (
                    getattr(user_info, "nick_name", None)
                    or getattr(user_info, "email", None)
                    or "User"
                )
                title = f"{user_name} - {home_name}"

                return self.async_create_entry(
                    title=title,
                    data=config_data,
                )

            # Handle re-authentication
            entry = self._get_reauth_entry()
            if entry is None:
                return self.async_abort(reason="reauth_entry_not_found")
            
            # Check if user_id matches (for security)
            if entry.data.get(CONF_USER_ID) != self._auth_info.user_info.user_id:
                return self.async_abort(reason="reauth_user_mismatch")
            
            # Update with new unique_id format if needed
            old_unique_id = entry.data.get(CONF_HOME_ID)
            new_unique_id = f"{self._auth_info.user_info.user_id}_{selected_home_id}"
            
            return self.async_update_reload_and_abort(
                entry,
                data_updates={
                    **self._auth_info.auth_data,
                    CONF_HOME_ID: selected_home_id,
                    CONF_USER_ID: self._auth_info.user_info.user_id,
                },
                unique_id=new_unique_id,
            )

        # Show home selection form
        return self.async_show_form(
            step_id="select_home",
            data_schema=self._get_home_selection_schema(),
            description_placeholders={
                "user_email": getattr(self._auth_info.user_info, "email", None)
                or "User",
            },
        )

    def _get_home_selection_schema(self) -> vol.Schema:
        """Get home selection schema."""
        homes = self._auth_info.homes

        if not homes:
            return vol.Schema({})

        home_options = {}
        for home in homes:
            home_id = getattr(home, "home_id", "")
            home_name = getattr(home, "home_name", "Unknown")
            device_count = getattr(home, "device_count", 0)

            display_text = f"{home_name} [{device_count} devices]"
            home_options[home_id] = display_text

        return vol.Schema(
            {
                vol.Required(CONF_HOME_ID): vol.In(home_options),
            }
        )

    async def async_step_reauth(
        self, entry_data: Mapping[str, Any]
    ) -> ConfigFlowResult:
        """Perform reauth upon migration of old entries."""
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Confirm reauth dialog."""
        if user_input is None:
            return self.async_show_form(
                step_id="reauth_confirm",
            )
        return await self.async_step_user()
