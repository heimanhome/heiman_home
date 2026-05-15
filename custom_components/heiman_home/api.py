"""API wrapper for Heiman integration."""

from __future__ import annotations

import logging
from typing import Any

from heimanconnect import (
    ChildDeviceManager,
    HeimanAuthError,
    HeimanCloudClient,
    HeimanConnectionError,
    HeimanDevice,
    HeimanHome,
    HeimanHttpClient,
    HeimanMqttClient,
    HeimanUser,
)

from homeassistant.core import HomeAssistant
from homeassistant.exceptions import (
    ConfigEntryAuthFailed,
    OAuth2TokenRequestReauthError,
    OAuth2TokenRequestTransientError,
)
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session
from homeassistant.helpers.update_coordinator import UpdateFailed

from .const import API_BASE_URL

_LOGGER = logging.getLogger(__name__)


class HeimanApiClient:
    """Heiman API client for Home Assistant."""

    def __init__(
        self,
        hass: HomeAssistant,
        session: OAuth2Session | None = None,
        token_data: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the API client.

        Args:
            hass: Home Assistant instance
            session: OAuth2 session for token management
            token_data: Token data for temporary use (e.g., during config flow)
        """
        self.hass = hass
        self._session = session
        self._token_data = token_data

        # Initialize HTTP and cloud clients
        self._http_client: HeimanHttpClient | None = None
        self._cloud_client: HeimanCloudClient | None = None
        self._mqtt_client: HeimanMqttClient | None = None
        self._child_device_manager: ChildDeviceManager | None = None

        self._initialize_clients()

    def _initialize_clients(self) -> None:
        """Initialize HTTP and cloud clients."""
        access_token = self._get_access_token()

        if not access_token:
            _LOGGER.warning("No access token available")
            return

        self._http_client = HeimanHttpClient(
            api_url=API_BASE_URL, access_token=access_token
        )

        self._cloud_client = HeimanCloudClient(
            http_client=self._http_client,
        )

        # Note: MQTT client will be initialized when needed with proper parameters
        # as it requires user_id and other runtime information

    def _get_access_token(self) -> str | None:
        """Get current access token."""
        if self._session and self._session.token:
            return self._session.token.get("access_token")
        if self._token_data:
            return self._token_data.get("access_token")
        return None

    async def _ensure_authenticated(self) -> None:
        """Ensure we have a valid access token."""
        if self._session:
            try:
                await self._session.async_ensure_token_valid()
            except OAuth2TokenRequestReauthError as err:
                # Token is invalid/expired, requires re-authentication
                _LOGGER.error(
                    "Token refresh failed, re-authentication required: %s", err
                )
                raise ConfigEntryAuthFailed(
                    "Token expired, please re-authenticate"
                ) from err
            except OAuth2TokenRequestTransientError as err:
                # Temporary error (network issue), should retry
                _LOGGER.debug("Token refresh transient error, will retry: %s", err)
                raise UpdateFailed(f"Temporary token refresh error: {err}") from err
            except Exception as err:
                # Unexpected error
                _LOGGER.exception("Unexpected error during token refresh")
                raise UpdateFailed(f"Token refresh failed: {err}") from err

        # Re-initialize client if token updated
        current_token = self._get_access_token()
        if self._http_client and current_token:
            self._http_client.update_access_token(current_token)

    async def async_get_user_info(self) -> HeimanUser:
        """Get current user information.

        Returns:
            HeimanUser object with user details

        Raises:
            ConfigEntryAuthFailed: If authentication fails
            UpdateFailed: If network request fails
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            raise HeimanConnectionError("Client not initialized")

        try:
            user = await self._cloud_client.async_get_user_info()
        except HeimanAuthError as err:
            raise ConfigEntryAuthFailed(f"Authentication failed: {err}") from err
        except HeimanConnectionError as err:
            raise UpdateFailed(f"Connection error getting user info: {err}") from err
        except Exception as err:
            _LOGGER.exception("Unexpected error getting user info")
            raise HeimanConnectionError(f"Failed to get user info: {err}") from err
        else:
            _LOGGER.debug("Retrieved user info: %s", user.email)
            return user

    async def async_get_homes(self) -> list[HeimanHome]:
        """Get list of homes for current user.

        Returns:
            List of HeimanHome objects

        Raises:
            ConfigEntryAuthFailed: If authentication fails
            UpdateFailed: If network request fails
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            raise HeimanConnectionError("Client not initialized")

        try:
            homes = await self._cloud_client.async_get_homes()
        except HeimanAuthError as err:
            raise ConfigEntryAuthFailed(f"Authentication failed: {err}") from err
        except HeimanConnectionError as err:
            raise UpdateFailed(f"Connection error getting homes: {err}") from err
        except Exception as err:
            _LOGGER.exception("Unexpected error getting homes")
            raise HeimanConnectionError(f"Failed to get homes: {err}") from err
        else:
            _LOGGER.debug("Retrieved %d homes", len(homes))
            return homes

    async def async_get_devices(self, home_id: str) -> dict[str, HeimanDevice]:
        """Get list of devices in specified home.

        Args:
            home_id: Home ID to fetch devices from

        Returns:
            Dictionary mapping device_id to HeimanDevice objects

        Raises:
            ConfigEntryAuthFailed: If authentication fails
            UpdateFailed: If network request fails
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            raise HeimanConnectionError("Client not initialized")

        try:
            # Set current home ID
            self._cloud_client.home_id = home_id
            devices = await self._cloud_client.async_get_devices(home_id=home_id)
        except HeimanAuthError as err:
            raise ConfigEntryAuthFailed(f"Authentication failed: {err}") from err
        except HeimanConnectionError as err:
            raise UpdateFailed(f"Connection error getting devices: {err}") from err
        except Exception as err:
            _LOGGER.exception("Unexpected error getting devices")
            raise HeimanConnectionError(f"Failed to get devices: {err}") from err
        else:
            _LOGGER.debug("Retrieved %d devices", len(devices))
            return devices

    async def async_get_device_properties(self, device_id: str) -> dict[str, Any]:
        """Get current properties of a device.

        Args:
            device_id: Device ID

        Returns:
            Dictionary of property identifier to value

        Raises:
            ConfigEntryAuthFailed: If authentication fails
            UpdateFailed: If network request fails
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            raise HeimanConnectionError("Client not initialized")

        try:
            properties = await self._cloud_client.async_get_device_properties(device_id)
        except HeimanAuthError as err:
            raise ConfigEntryAuthFailed(f"Authentication failed: {err}") from err
        except HeimanConnectionError as err:
            raise UpdateFailed(
                f"Connection error getting device properties: {err}"
            ) from err
        except Exception as err:
            _LOGGER.exception("Unexpected error getting device properties")
            raise HeimanConnectionError(
                f"Failed to get device properties: {err}"
            ) from err
        else:
            _LOGGER.debug(
                "Retrieved properties for device %s: %s", device_id, properties
            )
            return properties

    async def async_control_device(
        self,
        device_id: str,
        property_identifier: str,
        value: Any,
    ) -> bool:
        """Control device by setting property value.

        Args:
            device_id: Target device ID
            property_identifier: Property to control
            value: Value to set

        Returns:
            True if control successful

        Raises:
            ConfigEntryAuthFailed: If authentication fails
            UpdateFailed: If network request fails
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            raise HeimanConnectionError("Client not initialized")

        try:
            result = await self._cloud_client.async_control_device(
                device_id=device_id,
                property_identifier=property_identifier,
                value=value,
            )
        except HeimanAuthError as err:
            raise ConfigEntryAuthFailed(f"Authentication failed: {err}") from err
        except HeimanConnectionError as err:
            raise UpdateFailed(f"Connection error controlling device: {err}") from err
        except Exception as err:
            _LOGGER.exception("Unexpected error controlling device")
            raise HeimanConnectionError(f"Failed to control device: {err}") from err
        else:
            _LOGGER.debug(
                "Successfully controlled device %s: %s=%s",
                device_id,
                property_identifier,
                value,
            )
            return result

    async def async_get_device_detail(self, device_id: str) -> dict[str, Any] | None:
        """Get detailed device information.

        Args:
            device_id: Device ID

        Returns:
            Dictionary with device details or None if not available

        Note:
            This method uses the internal _async_get_device_detail from heimanconnect
            library as there is no public API available. This is necessary to access
            deriveMetadata which contains real-time property values.
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            _LOGGER.warning("Cloud client not initialized")
            return None

        try:
            # Use the internal method to get device detail
            # Note: This accesses a private method from heimanconnect library
            # because deriveMetadata (containing property values) is only available
            # through this internal endpoint
            # return await self._cloud_client._async_get_device_detail(device_id)  # noqa: SLF001
            return await self._cloud_client._async_get_device_detail(device_id)  # noqa: SLF001
        except Exception as err:  # noqa: BLE001
            _LOGGER.debug("Failed to get device detail for %s: %s", device_id, err)
            return None

    async def async_get_device_firmware_info(
        self,
        device_id: str,
        product_id: str | None = None,
        device_name: str | None = None,
        current_version: str | None = None,
    ) -> dict[str, Any] | None:
        """Get firmware information for a device.

        Args:
            device_id: Device ID
            product_id: Product ID (optional)
            device_name: Device name (optional)
            current_version: Current firmware version (optional)

        Returns:
            Firmware information dictionary or None if not available
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            _LOGGER.warning("Cloud client not initialized")
            return None

        try:
            return await self._cloud_client.async_get_device_firmware_info(
                device_id=device_id,
                product_id=product_id,
                device_name=device_name,
                current_version=current_version,
            )
        except Exception as err:  # noqa: BLE001
            _LOGGER.debug(
                "Failed to get firmware info for %s: %s",
                device_id,
                err,
            )
            return None

    async def async_confirm_firmware_upgrade(
        self,
        device_id: str,
        product_id: str | None = None,
        device_name: str | None = None,
        current_version: str | None = None,
    ) -> dict[str, Any]:
        """Confirm and start firmware upgrade for a device.

        Args:
            device_id: Device ID to upgrade
            product_id: Product ID (optional)
            device_name: Device name (optional)
            current_version: Current firmware version (optional)

        Returns:
            Upgrade confirmation response
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            msg = "Cloud client not initialized"
            raise HeimanConnectionError(msg)

        return await self._cloud_client.async_confirm_firmware_upgrade(
            device_id=device_id,
            product_id=product_id,
            device_name=device_name,
            current_version=current_version,
        )

    async def async_get_firmware_upgrade_history(
        self,
        device_id: str,
    ) -> dict[str, Any] | None:
        """Get firmware upgrade history/progress for a device.

        Args:
            device_id: Device ID to query upgrade history

        Returns:
            Firmware upgrade history/progress information or None
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            _LOGGER.warning("Cloud client not initialized")
            return None

        try:
            return await self._cloud_client.async_get_firmware_upgrade_history(
                device_id=device_id,
            )
        except Exception as err:  # noqa: BLE001
            _LOGGER.debug(
                "Failed to get firmware upgrade history for %s: %s",
                device_id,
                err,
            )
            return None

    async def async_get_devices_firmware_list(
        self,
        device_ids: list[str],
    ) -> list[dict[str, Any]]:
        """Get list of devices with pending firmware upgrades.

        Args:
            device_ids: List of device IDs to check for pending upgrades

        Returns:
            List of device information with firmware upgrade details
        """
        await self._ensure_authenticated()

        if not self._cloud_client:
            _LOGGER.warning("Cloud client not initialized")
            return []

        try:
            return await self._cloud_client.async_get_devices_firmware_list(
                device_ids=device_ids,
            )
        except Exception as err:  # noqa: BLE001
            _LOGGER.debug(
                "Failed to get devices firmware list: %s",
                err,
            )
            return []

    async def close(self) -> None:
        """Close the client."""
        if self._http_client:
            await self._http_client.close()
        
        # Disconnect MQTT client if connected
        if self._mqtt_client and self._mqtt_client.is_connected:
            await self._mqtt_client.disconnect()
    
    async def _initialize_mqtt_client(
        self,
        user_id: str,
        devices: dict[str, Any] | None = None,
        user_display_name: str | None = None,
    ) -> HeimanMqttClient:
        """Initialize MQTT client if not already initialized.
        
        Args:
            user_id: User ID for MQTT subscription
            devices: Dictionary of devices for child device detection
            user_display_name: User display name for device control payload
            
        Returns:
            HeimanMqttClient instance
        """
        if self._mqtt_client is None or not self._mqtt_client.is_connected:
            access_token = self._get_access_token()
            
            if not access_token:
                raise HeimanConnectionError("No access token available for MQTT")
            
            self._mqtt_client = HeimanMqttClient(
                hass=self.hass,
                access_token=access_token,
                user_id=user_id,
                user_display_name=user_display_name,
                cloud_client=self._cloud_client,
                devices=devices,
            )
            
            # Connect to MQTT broker
            await self._mqtt_client.connect()
            _LOGGER.info("MQTT client initialized and connected")
        
        return self._mqtt_client
    
    async def async_get_child_device_manager(
        self,
        user_id: str,
        devices: dict[str, Any] | None = None,
        user_display_name: str | None = None,
    ) -> ChildDeviceManager:
        """Get child device manager instance with initialized MQTT client.
        
        This method ensures the MQTT client is properly initialized before
        returning the child device manager.
        
        Args:
            user_id: User ID for MQTT subscription
            devices: Dictionary of devices for child device detection
            user_display_name: User display name for device control payload
            
        Returns:
            ChildDeviceManager instance with initialized MQTT client
        """
        mqtt_client = await self._initialize_mqtt_client(
            user_id=user_id,
            devices=devices,
            user_display_name=user_display_name,
        )
        
        # Create child device manager with the initialized MQTT client
        self._child_device_manager = ChildDeviceManager(mqtt_client=mqtt_client)
        
        return self._child_device_manager
