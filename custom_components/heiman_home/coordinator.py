"""Data update coordinator for Heiman integration."""

from __future__ import annotations

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any

from heimanconnect import (
    DeviceManagement,
    DeviceProperty,
    HeimanDevice,
    HeimanHome,
    HeimanMqttClient,
    HeimanMQTTError,
    HeimanUser,
)
from heimanconnect.utils import update_device_property_from_metadata
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_TOKEN
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import HeimanApiClient
from .const import CONF_HOME_ID, CONF_USER_ID, DOMAIN

_LOGGER = logging.getLogger(__name__)

# Polling interval: 30 minutes
# MQTT handles real-time property updates, but we need periodic polling for:
# - Device online/offline status
# - New device detection
# - Firmware version updates
UPDATE_INTERVAL = timedelta(minutes=30)
MQTT_RECONNECT_BASE_DELAY = 10
MQTT_RECONNECT_MAX_DELAY = 60
MQTT_CONNECTED_CHECK_INTERVAL = 30


def _infer_entity_type(prop_value: Any) -> str | None:
    """Infer the appropriate entity type from a property value.

    Args:
        prop_value: The property value to analyze.

    Returns:
        The entity type string (e.g., "sensor") or None for auto-detection.

    Note:
        Boolean values should NOT default to "sensor" - they should be
        left as None so other entity platforms (switch, binary_sensor)
        can handle them appropriately based on device metadata.
    """
    if isinstance(prop_value, bool):
        # Boolean values should not be forced to sensor.
        # Leave as None for auto-detection by other entity platforms.
        return None
    if isinstance(prop_value, (int, float)):
        # Numeric values are typically sensors
        return "sensor"
    # String and other types: let entity auto-detection handle it
    return None


@dataclass
class HeimanData:
    """Container for Heiman data."""

    user_info: HeimanUser | None = None
    home_info: HeimanHome | None = None
    devices: dict[str, HeimanDevice] = field(default_factory=dict)
    last_update: datetime | None = None
    errors: dict[str, str] = field(default_factory=dict)


class HeimanDataUpdateCoordinator(DataUpdateCoordinator[HeimanData]):
    """Heiman data update coordinator."""

    config_entry: ConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        logger: logging.Logger,
        api_client: HeimanApiClient,
        config_entry: ConfigEntry,
        device_management: DeviceManagement | None = None,
        oauth_session=None,
    ) -> None:
        """Initialize the coordinator.

        Args:
            hass: Home Assistant instance
            logger: Logger instance
            api_client: API client instance
            config_entry: Config entry instance
            device_management: Device management instance
            oauth_session: OAuth2 session for token retrieval
        """
        super().__init__(
            hass=hass,
            logger=logger,
            config_entry=config_entry,
            name="Heiman Home",
            update_interval=UPDATE_INTERVAL,
        )

        self.api_client = api_client
        self.config_entry = config_entry
        self.device_management = device_management
        self.data = HeimanData()
        self.mqtt_client: HeimanMqttClient | None = None
        self.oauth_session = oauth_session
        # Cache for device details to avoid N+1 API calls
        self._device_detail_cache: dict[str, dict[str, Any] | None] = {}
        self._device_detail_cache_timestamp: datetime | None = None
        # Cache TTL: 5 minutes
        self._device_detail_cache_ttl = 300
        # Cache for all ever-seen devices to prevent "device not found" errors
        # when devices are filtered out but entities still reference them
        self._all_devices_cache: dict[str, HeimanDevice] = {}
        # Counter for MQTT reconnect attempts
        self._mqtt_reconnect_attempts: int = 0
        self._mqtt_connect_lock = asyncio.Lock()
        self._mqtt_reconnect_task: asyncio.Task | None = None
        self._mqtt_reconnect_shutdown = False

    async def _async_update_data(self) -> HeimanData:
        """Fetch data from Heiman API.

        Returns:
            HeimanData object with updated information

        Raises:
            ConfigEntryAuthFailed: If authentication fails
            UpdateFailed: If data fetch fails
        """
        try:
            # Get home ID
            home_id = self.config_entry.data.get(CONF_HOME_ID)
            if not home_id:
                msg = "Home ID not found in config entry"
                raise UpdateFailed(msg)  # noqa: TRY301

            # Clear errors at the start of update, then repopulate as we go
            # This allows partial failures to be observable
            self.data.errors.clear()

            # Fetch user and home info on first update
            await self._fetch_user_and_home_info()

            # Get and process devices
            await self._fetch_and_process_devices(home_id)

            # Update last update time
            self.data.last_update = datetime.now(UTC)

        except ConfigEntryAuthFailed:
            _LOGGER.error("Authentication failed during data update")
            raise
        except UpdateFailed:
            # Re-raise UpdateFailed as-is to preserve retry_after and message
            raise
        except TimeoutError as err:
            _LOGGER.error("Timeout during data update: %s", err)
            if self.data.devices:
                # Graceful degradation: keep cached devices alive
                _LOGGER.warning(
                    "Timeout error, but %d cached devices exist. "
                    "Keeping existing data to avoid mass unavailability.",
                    len(self.data.devices),
                )
                self.data.errors["timeout"] = str(err)
                return self.data
            raise UpdateFailed(f"Heiman API request timed out: {err}") from err
        except OSError as err:
            _LOGGER.error("Network error during data update: %s", err)
            if self.data.devices:
                _LOGGER.warning(
                    "Network error, but %d cached devices exist. "
                    "Keeping existing data to avoid mass unavailability.",
                    len(self.data.devices),
                )
                self.data.errors["network"] = str(err)
                return self.data
            raise UpdateFailed(f"Heiman API network error: {err}") from err
        except Exception as err:
            _LOGGER.exception(
                "Unexpected error during data update: %s (type=%s)",
                err,
                type(err).__name__,
            )
            # Graceful degradation: if we already have device data from a
            # previous successful update, return it so entities stay available.
            # Only raise UpdateFailed (which marks everything unavailable)
            # when there is genuinely no cached data to fall back on.
            if self.data.devices:
                _LOGGER.warning(
                    "Unexpected error, but %d cached devices exist. "
                    "Keeping existing data to avoid mass unavailability. "
                    "Error details: %s",
                    len(self.data.devices),
                    err,
                )
                self.data.errors["unexpected"] = f"{type(err).__name__}: {err}"
                return self.data
            raise UpdateFailed(f"Error fetching Heiman data: {err}") from err

        return self.data

    async def _fetch_user_and_home_info(self) -> None:
        """Fetch user and home information on first update.

        Failures in user_info are downgraded to warnings instead of
        raising UpdateFailed, so that a transient user-info error does
        not mark every device entity unavailable.
        """
        # Get user info (only on first update)
        if self.data.user_info is None:
            try:
                self.data.user_info = await self.api_client.async_get_user_info()
            except ConfigEntryAuthFailed:
                raise
            except Exception as err:
                _LOGGER.warning(
                    "Failed to fetch user info: %s. "
                    "Devices will remain available, but user-dependent features "
                    "(e.g. MQTT display name) may be degraded.",
                    err,
                )
                self.data.errors["user_info"] = str(err)
                # Do NOT raise UpdateFailed here – let device fetching continue.
                # The coordinator stays healthy and entities remain available.

        # Get home info (only on first update)
        if self.data.home_info is None:
            try:
                homes = await self.api_client.async_get_homes()
                if homes:
                    home_id = self.config_entry.data.get(CONF_HOME_ID)
                    self.data.home_info = next(
                        (h for h in homes if h.home_id == home_id),
                        homes[0],
                    )
            except ConfigEntryAuthFailed:
                raise
            except Exception as err:  # noqa: BLE001
                _LOGGER.warning("Failed to fetch home info: %s", err)
                self.data.errors["home_info"] = str(err)

    async def _fetch_and_process_devices(self, home_id: str) -> None:
        """Fetch and process device data."""
        try:
            devices_dict = await self.api_client.async_get_devices(home_id=home_id)

            # Update all devices cache before filtering
            # This ensures entities can still find devices even if they are filtered out
            for device_id, device in devices_dict.items():
                self._all_devices_cache[device_id] = device

            # Evict devices that no longer exist in API response
            # This prevents stale devices from persisting forever
            current_device_ids = set(devices_dict.keys())
            cached_device_ids = set(self._all_devices_cache.keys())
            stale_device_ids = cached_device_ids - current_device_ids
            if stale_device_ids:
                _LOGGER.debug("Evicting stale devices from cache: %s", stale_device_ids)
                for device_id in stale_device_ids:
                    del self._all_devices_cache[device_id]

            # Apply device filtering
            if self.device_management:
                devices_list = list(devices_dict.values())
                filtered_devices_list = (
                    self.device_management.filter_manager.get_filtered_devices(
                        devices_list
                    )
                )
                # Convert back to dictionary
                devices = {d.device_id: d for d in filtered_devices_list}
            else:
                devices = devices_dict

            # Extract firmware version from device list
            self._extract_firmware_versions(devices)

            # Get detailed info for filtered devices to populate property values
            await self._update_device_details(devices)

            # Check for firmware updates (batch request)
            await self._check_firmware_updates_batch(devices)

            # Update device data and merge old states
            self._merge_device_states(devices)

        except ConfigEntryAuthFailed:
            raise
        except UpdateFailed:
            # Re-raise UpdateFailed as-is to preserve retry_after and message
            raise
        except Exception as err:
            _LOGGER.exception("Failed to fetch devices")
            self.data.errors["devices"] = str(err)
            # If there was previous device data, keep it
            if not self.data.devices:
                msg = f"Failed to fetch devices: {err}"
                raise UpdateFailed(msg) from err

    def _extract_firmware_versions(self, devices: dict[str, HeimanDevice]) -> None:
        """Extract firmware versions from device data."""
        for device in devices.values():
            # First check if device raw_data has firmwareInfo
            if hasattr(device, "raw_data") and device.raw_data:
                firmware_info = device.raw_data.get("firmwareInfo", {})
                if isinstance(firmware_info, dict) and "version" in firmware_info:
                    device.firmware_version = firmware_info.get("version")

            # Try to get firmware version from device's firmware_info attribute
            if hasattr(device, "firmware_info") and device.firmware_info:
                if (
                    isinstance(device.firmware_info, dict)
                    and "version" in device.firmware_info
                ):
                    device.firmware_version = device.firmware_info.get("version")

    async def _check_firmware_updates_batch(
        self, devices: dict[str, HeimanDevice]
    ) -> None:
        """Check for firmware updates for all devices in a batch request.

        This method uses the heimanconnect library's batch firmware check API
        to efficiently check multiple devices at once instead of individual requests.

        Args:
            devices: Dictionary of device_id to HeimanDevice objects
        """
        if not devices:
            return

        try:
            # Get list of device IDs
            device_ids = list(devices.keys())

            # Batch request to check which devices have pending firmware upgrades
            firmware_list = await self.api_client.async_get_devices_firmware_list(
                device_ids=device_ids,
            )

            if not firmware_list:
                _LOGGER.debug("No devices with pending firmware upgrades")
                return

            _LOGGER.info(
                "Found %d devices with available firmware updates",
                len(firmware_list),
            )

            # Process each device with available update
            for device_info in firmware_list:
                device_id = device_info.get("deviceId") or device_info.get("id")
                if not device_id or device_id not in devices:
                    continue

                device = devices[device_id]

                # Extract latest version info from multiple possible locations
                latest_version = (
                    device_info.get("latestVersion")
                    or device_info.get("newVersion")
                    or device_info.get("targetVersion")
                )

                # If not found in direct fields, check upgradeTasks
                if not latest_version:
                    upgrade_tasks = device_info.get("upgradeTasks", [])
                    if upgrade_tasks and isinstance(upgrade_tasks, list):
                        # Get the first upgrade task
                        first_task = upgrade_tasks[0]
                        if isinstance(first_task, dict):
                            latest_version = first_task.get("upgradeVersion")

                if latest_version:
                    # Store firmware upgrade info in device for update entity to use
                    if not hasattr(device, "firmware_upgrade_info"):
                        device.firmware_upgrade_info = {}  # type: ignore[attr-defined]

                    device.firmware_upgrade_info = {  # type: ignore[attr-defined]
                        "latest_version": latest_version,
                        "current_version": device.firmware_version,
                        "update_available": True,
                        "description": device_info.get("description")
                        or device_info.get("releaseNotes")
                        or device_info.get("changeLog"),
                    }

                    _LOGGER.info(
                        "Firmware update available for %s: %s -> %s",
                        device.device_name,
                        device.firmware_version,
                        latest_version,
                    )

        except Exception as err:  # noqa: BLE001
            _LOGGER.debug(
                "Failed to check firmware updates batch: %s",
                err,
            )
            # Don't raise exception - firmware check is optional

    async def _update_device_details(self, devices: dict[str, HeimanDevice]) -> None:
        """Update device details including properties from deriveMetadata.

        Uses caching to avoid N+1 API calls. Cache is invalidated every 5 minutes
        or when a device is not found in cache. Fetches device details concurrently
        with a limit of 5 concurrent requests to prevent overwhelming the API.
        """
        now = datetime.now(UTC)

        # Check if cache needs refresh
        cache_expired = (
            self._device_detail_cache_timestamp is None
            or (now - self._device_detail_cache_timestamp).total_seconds()
            > self._device_detail_cache_ttl
        )

        # If cache expired, clear it
        if cache_expired:
            self._device_detail_cache.clear()
            self._device_detail_cache_timestamp = now

        # Process cached device details first so deriveMetadata is applied even
        # when only some devices need fetching.
        for device_id, device in devices.items():
            device_detail = self._device_detail_cache.get(device_id)
            if device_detail:
                self._process_device_detail(device, device_detail)

        # Identify devices that need detail fetching (not in cache)
        devices_to_fetch = [
            device_id
            for device_id in devices
            if device_id not in self._device_detail_cache
        ]

        if not devices_to_fetch:
            return

        # Create a semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(5)

        async def fetch_device_detail(
            device_id: str,
        ) -> tuple[str, dict[str, Any] | None]:
            """Fetch device detail with concurrency control."""
            async with semaphore:
                try:
                    device_detail = await self.api_client.async_get_device_detail(
                        device_id
                    )
                except Exception as err:  # noqa: BLE001
                    _LOGGER.debug(
                        "Failed to get device details for %s: %s",
                        device_id,
                        err,
                    )
                    return device_id, None

                return device_id, device_detail

        # Fetch all device details concurrently
        results = await asyncio.gather(
            *[fetch_device_detail(device_id) for device_id in devices_to_fetch],
            return_exceptions=False,
        )

        # Process results and update cache
        for device_id, device_detail in results:
            # Cache the result (including None for failed requests)
            self._device_detail_cache[device_id] = device_detail

            # Process the detail if available
            if device_detail and device_id in devices:
                self._process_device_detail(devices[device_id], device_detail)

    def _process_device_detail(
        self, device: HeimanDevice, device_detail: dict[str, Any]
    ) -> None:
        """Process device detail and update properties."""
        # Extract firmware version from firmwareInfo (if not retrieved earlier)
        if not device.firmware_version:
            firmware_info = device_detail.get("firmwareInfo", {})
            if isinstance(firmware_info, dict) and "version" in firmware_info:
                device.firmware_version = firmware_info.get("version")

        # Extract property values from deriveMetadata and update device object
        if "deriveMetadata" in device_detail:
            try:
                metadata_str = device_detail.get("deriveMetadata", "")
                if metadata_str:
                    # deriveMetadata is a JSON string that parses to a list of property objects
                    metadata_list = json.loads(metadata_str)

                    # Iterate through the list and update properties
                    if isinstance(metadata_list, list):
                        for prop_item in metadata_list:
                            update_device_property_from_metadata(device, prop_item)
            except Exception:
                _LOGGER.exception(
                    "Failed to parse deriveMetadata for %s", device.device_id
                )

    def _update_device_property(
        self, device: HeimanDevice, prop_item: dict[str, Any]
    ) -> None:
        """Update a single device property from metadata."""
        prop_id = prop_item.get("property", "") or prop_item.get("id", "")
        prop_value = prop_item.get("value")

        if not prop_id or prop_value is None:
            return

        # Special handling for DeviceINFO object
        if prop_id == "DeviceINFO" and isinstance(prop_value, dict):
            self._process_device_info(device, prop_value)
        elif prop_id in device.properties:
            # Update regular property
            if prop_id == "RSSI":
                # Preserve RSSI as the raw numeric dBm value
                device.properties[prop_id].value = self._convert_dbm_to_level(
                    prop_value
                )
            else:
                device.properties[prop_id].value = prop_value

    def _process_device_info(
        self, device: HeimanDevice, device_info: dict[str, Any]
    ) -> None:
        """Process DeviceINFO nested structure."""
        # Extract MAC address
        mac_value = device_info.get("MAC")
        if mac_value and "DeviceINFO_MAC" in device.properties:
            device.properties["DeviceINFO_MAC"].value = mac_value

        # Extract DBM (signal strength in dBm)
        dbm_value = device_info.get("DBM")
        if dbm_value is not None and "DeviceINFO_DBM" in device.properties:
            device.properties["DeviceINFO_DBM"].value = dbm_value

        # Extract DBM_Level (signal strength level)
        dbm_level_value = device_info.get("DBM_Level")
        if dbm_level_value is None and dbm_value is not None:
            # Convert numeric DBM to level string if DBM_Level not provided
            dbm_level_value = self._convert_dbm_to_level(dbm_value)

        if dbm_level_value is not None:
            # Update existing property or create if it doesn't exist
            if "DeviceINFO_DBM_Level" in device.properties:
                device.properties["DeviceINFO_DBM_Level"].value = dbm_level_value
            else:
                # Create the property if it doesn't exist
                dbm_property = device.properties.get("DeviceINFO_DBM")
                device.properties["DeviceINFO_DBM_Level"] = DeviceProperty(
                    identifier="DeviceINFO_DBM_Level",
                    name="DBM Level",
                    value=dbm_level_value,
                    readable=getattr(dbm_property, "readable", True),
                    entity=getattr(dbm_property, "entity", "sensor"),
                )

        # Extract IP address
        ip_value = device_info.get("IP")
        if ip_value and "DeviceINFO_IP" in device.properties:
            device.properties["DeviceINFO_IP"].value = ip_value

    def _merge_device_states(self, devices: dict[str, HeimanDevice]) -> None:
        """Merge old device states with new device data."""
        old_devices = self.data.devices.copy()
        self.data.devices = devices

        # Merge old device states (preserve old values only when new values are None)
        for device_id, new_device in devices.items():
            if device_id in old_devices:
                old_device = old_devices[device_id]
                # Preserve old device's online status and other dynamic properties
                for prop_id, old_prop in old_device.properties.items():
                    if prop_id not in new_device.properties:
                        # Keep runtime-discovered properties (e.g. MQTT-only fields)
                        # when they are not present in the next poll response.
                        new_device.properties[prop_id] = old_prop
                        continue

                    if prop_id in new_device.properties:
                        # Only copy old value if new value is None
                        if (
                            new_device.properties[prop_id].value is None
                            and old_prop.value is not None
                        ):
                            new_device.properties[prop_id].value = old_prop.value

                # Copy online status only when the new status is unknown
                if new_device.online is None and old_device.online is not None:
                    new_device.online = old_device.online

    def get_device(self, device_id: str) -> HeimanDevice | None:
        """Get device by ID.

        Args:
            device_id: Device ID to retrieve

        Returns:
            HeimanDevice object or None if not found
        """
        device = self.data.devices.get(device_id)
        if device is None:
            device = self._all_devices_cache.get(device_id)
        return device

    def get_all_devices(self) -> list[HeimanDevice]:
        """Get all devices.

        Returns:
            List of all HeimanDevice objects
        """
        return list(self.data.devices.values())

    def get_devices_by_type(self, device_type: str) -> list[HeimanDevice]:
        """Get devices by type.

        Args:
            device_type: Device type to filter by

        Returns:
            List of matching HeimanDevice objects
        """
        return [
            device
            for device in self.data.devices.values()
            if device.device_type == device_type
        ]

    @staticmethod
    def _convert_dbm_to_level(dbm_value: float) -> str:
        """Convert numeric DBM value to signal strength level string.

        Args:
            dbm_value: Signal strength in dBm (negative number)

        Returns:
            Signal level string: "strong", "medium", "weak", or "very_weak"
        """
        # DBM values are typically negative numbers
        # Closer to 0 = stronger signal
        if dbm_value >= -50:
            return "strong"
        if dbm_value >= -65:
            return "medium"
        if dbm_value >= -75:
            return "weak"
        return "very_weak"

    async def async_init_mqtt_client(self) -> None:
        """Initialize MQTT client for real-time updates."""
        self._start_mqtt_reconnect_monitor()
        await self._async_ensure_mqtt_connected()

    async def async_shutdown_mqtt_client(self) -> None:
        """Stop MQTT reconnect monitoring and disconnect the MQTT client."""
        self._mqtt_reconnect_shutdown = True

        if self._mqtt_reconnect_task:
            self._mqtt_reconnect_task.cancel()
            try:
                await self._mqtt_reconnect_task
            except asyncio.CancelledError:
                pass
            self._mqtt_reconnect_task = None

        await self._async_reset_mqtt_client()

    def _start_mqtt_reconnect_monitor(self) -> None:
        """Start background MQTT reconnect monitoring."""
        if self._mqtt_reconnect_task and not self._mqtt_reconnect_task.done():
            return

        self._mqtt_reconnect_shutdown = False
        self._mqtt_reconnect_task = self.hass.async_create_background_task(
            self._async_mqtt_reconnect_monitor(),
            name=f"{DOMAIN} MQTT reconnect monitor",
        )

    async def _async_mqtt_reconnect_monitor(self) -> None:
        """Continuously restore MQTT after network or broker outages."""
        delay = MQTT_CONNECTED_CHECK_INTERVAL

        while not self._mqtt_reconnect_shutdown:
            await asyncio.sleep(delay)

            if self._mqtt_reconnect_shutdown:
                return

            if self._is_mqtt_connected():
                self.data.errors.pop("mqtt", None)
                self._mqtt_reconnect_attempts = 0
                delay = MQTT_CONNECTED_CHECK_INTERVAL
                continue

            connected = await self._async_ensure_mqtt_connected(refresh_devices=True)
            if connected:
                delay = MQTT_CONNECTED_CHECK_INTERVAL
            else:
                delay = min(
                    MQTT_RECONNECT_BASE_DELAY
                    * (2 ** max(self._mqtt_reconnect_attempts - 1, 0)),
                    MQTT_RECONNECT_MAX_DELAY,
                )

    def _is_mqtt_connected(self) -> bool:
        """Return whether MQTT is currently connected."""
        return bool(
            self.mqtt_client and getattr(self.mqtt_client, "is_connected", False)
        )

    async def _async_ensure_mqtt_connected(
        self,
        *,
        refresh_devices: bool = False,
    ) -> bool:
        """Connect MQTT if needed and keep retry state for the monitor."""
        if self._is_mqtt_connected():
            return True

        async with self._mqtt_connect_lock:
            if self._is_mqtt_connected():
                return True

            if refresh_devices:
                await self._async_refresh_devices_for_mqtt()

            await self._async_reset_mqtt_client()

            connected = await self._async_connect_mqtt_client()
            if connected:
                self._mqtt_reconnect_attempts = 0
                self.data.errors.pop("mqtt", None)
                return True

            self._mqtt_reconnect_attempts += 1
            return False

    async def _async_connect_mqtt_client(self) -> bool:
        """Create and connect the MQTT client once."""
        try:
            # Get access token from config entry (preferred) or OAuth2 session.
            access_token = None
            user_id = self.config_entry.data.get(CONF_USER_ID)

            token_data = self.config_entry.data.get(CONF_TOKEN)
            if token_data and isinstance(token_data, dict):
                access_token = token_data.get("access_token")

            # Fallback: read token directly from OAuth2 session without
            # triggering a refresh (Heiman tokens never expire).
            if not access_token and self.oauth_session:
                try:
                    if self.oauth_session.token:
                        access_token = self.oauth_session.token.get("access_token")
                except Exception as err:  # noqa: BLE001
                    _LOGGER.warning(
                        "Failed to read access_token from OAuth2 session: %s", err
                    )

            if not access_token:
                _LOGGER.warning(
                    "Cannot initialize MQTT: access_token not available from any source"
                )
                return False

            if not user_id:
                _LOGGER.warning("Cannot initialize MQTT: user_id not available")
                return False

            # Get user display name (prefer nickName, fallback to email)
            user_display_name = None
            try:
                if self.data.user_info:
                    # Try to get nickName first
                    user_display_name = getattr(self.data.user_info, "nick_name", None)
                    if not user_display_name:
                        # Fallback to email
                        user_display_name = getattr(self.data.user_info, "email", None)
            except Exception as err:  # noqa: BLE001
                _LOGGER.warning("Failed to get user display name: %s", err)

            # Get cloud client reference for child device detection
            cloud_client = None
            try:
                # Note: Accessing _cloud_client is necessary because HeimanMqttClient
                # requires the cloud client instance to detect child devices.
                # This is an internal implementation detail that may be refactored
                # in future versions of heimanconnect library.
                if hasattr(self.api_client, "_cloud_client"):
                    cloud_client = self.api_client._cloud_client  # noqa: SLF001
            except Exception as err:  # noqa: BLE001
                _LOGGER.warning("Failed to get cloud_client reference: %s", err)

            # Get devices dictionary for child device detection
            # Use all devices cache to include both filtered and non-filtered devices
            devices_dict = (
                dict(self._all_devices_cache) if self._all_devices_cache else {}
            )

            self.mqtt_client = HeimanMqttClient(
                hass=self.hass,
                access_token=access_token,
                user_id=user_id,
                user_display_name=user_display_name,
                cloud_client=cloud_client,
                devices=devices_dict,
            )

            await self.mqtt_client.connect()

            self.mqtt_client.register_device_callback(self._on_device_property_update)

            if hasattr(self.mqtt_client, "register_online_callback"):
                self.mqtt_client.register_online_callback(self._on_device_status_change)
            else:
                _LOGGER.debug(
                    "MQTT online callback is not supported by this heimanconnect "
                    "version; online state will be refreshed by polling"
                )

            _LOGGER.info("MQTT client initialized and connected successfully")
            return True

        except HeimanMQTTError as err:
            _LOGGER.warning("Failed to connect MQTT client: %s", err)
            if "Name does not resolve" in str(err):
                _LOGGER.warning(
                    "DNS resolution failed. MQTT will retry in the background."
                )
            self.data.errors["mqtt"] = str(err)
        except Exception as err:  # noqa: BLE001
            _LOGGER.warning("Unexpected error connecting MQTT client: %s", err)
            self.data.errors["mqtt"] = f"{type(err).__name__}: {err}"

        await self._async_reset_mqtt_client()
        return False

    async def _async_refresh_devices_for_mqtt(self) -> None:
        """Refresh device metadata used to rebuild MQTT child-device topics."""
        try:
            _LOGGER.info("Refreshing device list before MQTT reconnect")

            home_id = self.config_entry.data.get(CONF_HOME_ID)
            if not home_id:
                _LOGGER.error("Home ID not found in config entry")
                return

            await self._fetch_and_process_devices(home_id)

        except Exception as err:  # noqa: BLE001
            _LOGGER.debug("Failed to refresh devices before MQTT reconnect: %s", err)

    async def _async_reset_mqtt_client(self) -> None:
        """Reset MQTT client to allow reinitialization."""
        if self.mqtt_client:
            try:
                if hasattr(self.mqtt_client, "disconnect"):
                    result = self.mqtt_client.disconnect()
                    if hasattr(result, "__await__"):
                        await result
            except Exception as err:  # noqa: BLE001
                _LOGGER.debug("Error disconnecting MQTT client: %s", err)

            self.mqtt_client = None

        _LOGGER.debug("MQTT client has been reset")

    def _on_device_property_update(
        self, device_id: str, properties: dict[str, Any]
    ) -> None:
        """Handle device property update from MQTT.

        Args:
            device_id: Device ID that sent the update
            properties: Dictionary of property name to value,
                or event data containing 'properties' or 'data' key
        """
        # Find device in coordinator data
        device = self.data.devices.get(device_id)
        if not device:
            return

        # Handle event format: extract properties from 'properties' or 'data' key
        actual_properties = properties
        if "properties" in properties and isinstance(properties["properties"], dict):
            actual_properties = properties["properties"]
            _LOGGER.debug("Extracted properties from event data: %s", actual_properties)
        elif "data" in properties and isinstance(properties["data"], dict):
            actual_properties = properties["data"]
            _LOGGER.debug(
                "Extracted properties from event data field: %s", actual_properties
            )

        # Update device properties with special handling
        for prop_name, prop_value in actual_properties.items():
            # Skip non-property fields
            if prop_name in [
                "event",
                "eventType",
                "deviceId",
                "messageId",
                "timestamp",
            ]:
                continue

            # Special handling for DeviceINFO object (same as _update_device_property)
            if prop_name == "DeviceINFO" and isinstance(prop_value, dict):
                self._process_device_info(device, prop_value)
            elif prop_name in device.properties:
                # Update regular property
                if prop_name == "RSSI":
                    # Preserve RSSI as the raw numeric dBm value
                    device.properties[prop_name].value = self._convert_dbm_to_level(
                        prop_value
                    )
                    _LOGGER.debug("RSSI: %s", device.properties[prop_name].value)
                else:
                    device.properties[prop_name].value = prop_value
                    _LOGGER.debug(
                        "Updated property %s to %s for device %s",
                        prop_name,
                        prop_value,
                        device_id,
                    )
            else:
                # Property doesn't exist in initial device properties
                # Log it but don't create new entity to avoid dynamic entity creation
                _LOGGER.debug(
                    "MQTT received new property %s for device %s, skipping entity creation",
                    prop_name,
                    device_id,
                )
                # Optionally store the value for debugging/monitoring
                # but don't add to properties dict to prevent entity creation
        _LOGGER.debug("Updated device properties: %s", device.properties)
        # Schedule entity update if coordinator is set up
        # IMPORTANT: Must be called from the event loop thread for thread safety
        if hasattr(self, "async_set_updated_data") and self.hass:
            # Use hass.add_job to schedule the update in the event loop
            # Pass the coroutine function and data as arguments
            self.hass.add_job(self.async_set_updated_data, self.data)

    def _on_device_status_change(
        self,
        device_id: str,
        is_online: bool,
        payload: dict,
    ) -> None:
        """Handle device online/offline status change from MQTT.

        Args:
            device_id: Device ID that changed status
            is_online: True if device is online, False if offline
            payload: Raw MQTT message payload
        """
        # Find device in coordinator data
        device = self.data.devices.get(device_id)
        if not device:
            _LOGGER.debug(
                "Device %s not found in coordinator data for status change", device_id
            )
            return

        # Update device online status
        device.online = is_online
        _LOGGER.info(
            "Device %s is now %s (via MQTT)",
            device.device_name or device_id,
            "online" if is_online else "offline",
        )

        # Schedule entity update if coordinator is set up
        if hasattr(self, "async_set_updated_data") and self.hass:
            self.hass.add_job(self.async_set_updated_data, self.data)

    async def async_read_device_properties(self, device_id: str) -> None:
        """Read properties from a specific device via MQTT.

        Args:
            device_id: Device ID to read properties from
        """
        if not self.mqtt_client:
            _LOGGER.warning("MQTT client not initialized, cannot read properties")
            return

        device = self.data.devices.get(device_id)
        if not device:
            _LOGGER.warning("Device %s not found in coordinator", device_id)
            return

        try:
            # Read all properties (empty list means read all)
            properties = await self.mqtt_client.async_read_properties(
                device_id=device_id,
                product_id=device.product_id,
                property_identifiers=None,  # Read all available properties
            )

            # Update device properties in coordinator data
            if properties:
                for prop_name, prop_value in properties.items():
                    if prop_name in device.properties:
                        device.properties[prop_name].value = prop_value
                    else:
                        # Property doesn't exist in initial device properties
                        # Log it but don't create new entity to avoid dynamic entity creation
                        _LOGGER.debug(
                            "Read properties returned new property %s"
                            " for device %s, skipping entity creation",
                            prop_name,
                            device_id,
                        )
                        # Optionally store the value for debugging/monitoring
                        # but don't add to properties dict to prevent entity creation

                # Trigger entity update
                # IMPORTANT: Must be called from the event loop thread for thread safety
                if hasattr(self, "async_set_updated_data") and self.hass:
                    # Use hass.add_job to schedule the update in the event loop
                    # Pass the coroutine function and data as arguments
                    self.hass.add_job(self.async_set_updated_data, self.data)
            else:
                _LOGGER.warning("No properties returned from device %s", device_id)

        except Exception as err:  # noqa: BLE001
            _LOGGER.error(
                "Failed to read properties from device %s: %s", device_id, err
            )

    def get_online_devices(self) -> list[HeimanDevice]:
        """Get all online devices.

        Returns:
            List of online HeimanDevice objects
        """
        return [device for device in self.data.devices.values() if device.online]

    def get_device_property(self, device_id: str, property_name: str) -> Any | None:
        """Get device property value from cache.

        Args:
            device_id: Device ID
            property_name: Property name

        Returns:
            Property value if found, None otherwise
        """
        device = self.data.devices.get(device_id)
        if not device:
            return None

        prop = device.properties.get(property_name)
        if not prop:
            return None

        return prop.value
