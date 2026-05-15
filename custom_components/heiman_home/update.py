"""Update platform for Heiman integration."""

from __future__ import annotations

import asyncio
import logging
from typing import Any

# Simple version comparison (assumes semantic versioning)
from packaging import version

from heimanconnect import HeimanDevice

from homeassistant import config_entries
from homeassistant.components.update import UpdateEntity, UpdateEntityFeature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import HeimanDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: config_entries.ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Heiman update entities based on a config entry."""
    coordinator: HeimanDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    # Track existing entities to avoid duplicates
    existing_entities: set[str] = set()

    def _create_update_entities_for_devices() -> None:
        """Create update entities for all devices and add new ones."""
        devices = coordinator.get_all_devices()
        new_update_entities = []

        for device in devices:
            unique_id = f"{device.device_id}_firmware_update"
            if unique_id not in existing_entities:
                new_update_entities.append(
                    HeimanUpdateEntity(
                        coordinator=coordinator,
                        device=device,
                    )
                )
                existing_entities.add(unique_id)

        if new_update_entities:
            async_add_entities(new_update_entities)

    # Initial setup
    _create_update_entities_for_devices()

    # Listen for coordinator updates to add new devices dynamically
    entry.async_on_unload(coordinator.async_add_listener(_create_update_entities_for_devices))


class HeimanUpdateEntity(CoordinatorEntity[HeimanDataUpdateCoordinator], UpdateEntity):
    """Representation of a Heiman update entity."""

    _attr_has_entity_name = True
    _attr_supported_features = (
        UpdateEntityFeature.INSTALL
        | UpdateEntityFeature.SPECIFIC_VERSION
        | UpdateEntityFeature.PROGRESS
    )

    def __init__(
        self,
        coordinator: HeimanDataUpdateCoordinator,
        device: HeimanDevice,
    ) -> None:
        """Initialize the update entity.

        Args:
            coordinator: Data coordinator
            device: Heiman device
        """
        super().__init__(coordinator)
        self._device = device

        _LOGGER.info(
            "Creating update entity for %s (device_id=%s)",
            device.device_name,
            device.device_id,
        )

        # Generate unique ID
        self._attr_unique_id = f"{device.device_id}_firmware_update"

        # Set name
        self._attr_name = "Firmware"

        # Extract firmware version - use multiple strategies
        sw_version = self._extract_firmware_version(device)

        # Get device info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.device_id)},
            name=device.device_name,
            manufacturer=device.manufacturer,
            model=device.model or device.product_id,
            sw_version=sw_version,
            hw_version=device.hardware_version,
        )

        # Initialize version attributes
        self._attr_installed_version = sw_version
        self._attr_latest_version = sw_version  # Default to current version
        self._attr_release_summary = None
        self._attr_release_url = None
        self._attr_title = "Heiman Firmware"
        self._attr_in_progress = False
        self._attr_update_percentage = None
        self._attr_auto_update = False
        
        # Cache for firmware upgrade info
        self._firmware_upgrade_info: dict[str, Any] | None = None
    
    def _extract_firmware_version(self, device: HeimanDevice) -> str | None:
        """Extract firmware version from device using multiple strategies.

        Args:
            device: Heiman device

        Returns:
            Firmware version string or None
        """
        sw_version = None

        # Strategy 1: Get directly from device.firmware_version attribute
        if hasattr(device, "firmware_version") and device.firmware_version:
            sw_version = device.firmware_version
            return sw_version

        # Strategy 2: Get from raw_data.firmwareInfo.version
        if hasattr(device, "raw_data") and device.raw_data:
            firmware_info = device.raw_data.get("firmwareInfo", {})
            if isinstance(firmware_info, dict) and firmware_info.get("version"):
                sw_version = firmware_info.get("version")
                return sw_version

        # Strategy 3: Get from firmware_info.version
        if hasattr(device, "firmware_info") and device.firmware_info:
            if isinstance(device.firmware_info, dict) and device.firmware_info.get("version"):
                sw_version = device.firmware_info.get("version")
                return sw_version

        # No firmware version found
        return sw_version
    
    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not self.coordinator.last_update_success:
            return False

        device = self.coordinator.get_device(self._device.device_id)
        if not device:
            return False

        return device.online is True
    
    @property
    def installed_version(self) -> str | None:
        """Return the current installed firmware version."""
        # Return cached version first
        if self._attr_installed_version:
            return self._attr_installed_version

        # Fallback to dynamic fetch
        device = self.coordinator.get_device(self._device.device_id)
        if not device:
            return None

        return self._extract_firmware_version(device)
    
    @property
    def latest_version(self) -> str | None:
        """Return the latest available firmware version.

        For now, we don't have a way to check for new firmware versions via API.
        This should be implemented when the API supports firmware update checks.
        """
        # Return cached latest version first
        if self._attr_latest_version:
            return self._attr_latest_version

        # Fallback to installed version (indicates no update available)
        return self.installed_version
    
    def _update_from_cache(self) -> bool:
        """Update entity state from coordinator cache (synchronous).

        Returns True if state was updated from cache, False if cache miss.
        """
        device = self.coordinator.get_device(self._device.device_id)
        if not device:
            _LOGGER.warning(
                "Update entity %s: device not found in coordinator",
                self._device.device_name,
            )
            return False

        # Get installed version
        installed_version = self._extract_firmware_version(device)
        _LOGGER.info(
            "Update entity %s: installed_version=%s, attr_installed_version=%s, device.firmware_version=%s",
            self._device.device_name,
            installed_version,
            self._attr_installed_version,
            getattr(device, 'firmware_version', 'N/A'),
        )
        
        if installed_version:
            # Only update if there's no better version
            if (
                not self._attr_installed_version
                or self._attr_installed_version == "unknown"
            ):
                self._attr_installed_version = installed_version

        # Check if coordinator has firmware upgrade info from batch check
        has_upgrade_info = hasattr(device, "firmware_upgrade_info") and device.firmware_upgrade_info
        _LOGGER.info(
            "Update entity %s: has_firmware_upgrade_info=%s",
            self._device.device_name,
            has_upgrade_info,
        )
        
        if has_upgrade_info:
            firmware_info = device.firmware_upgrade_info
            latest_version = firmware_info.get("latest_version")
            
            _LOGGER.info(
                "Update entity %s: firmware_upgrade_info=%s, latest_version=%s",
                self._device.device_name,
                firmware_info,
                latest_version,
            )
            
            if latest_version and self._attr_installed_version:
                # Compare versions
                is_newer = self._version_is_newer(latest_version, self._attr_installed_version)
                _LOGGER.info(
                    "Update entity %s: version comparison result: %s > %s = %s",
                    self._device.device_name,
                    latest_version,
                    self._attr_installed_version,
                    is_newer,
                )
                
                if is_newer:
                    self._attr_latest_version = latest_version
                    self._attr_release_summary = firmware_info.get("description")
                    _LOGGER.info(
                        "Firmware update available for %s (from batch check): %s -> %s",
                        self._device.device_name,
                        self._attr_installed_version,
                        latest_version,
                    )
                else:
                    # No update available
                    self._attr_latest_version = self._attr_installed_version
                    self._attr_release_summary = None
                    _LOGGER.debug(
                        "No firmware update for %s: installed=%s, latest=%s",
                        self._device.device_name,
                        self._attr_installed_version,
                        latest_version,
                    )

        # If no latest version, use installed version
        if installed_version and not self._attr_latest_version:
            self._attr_latest_version = installed_version

        _LOGGER.info(
            "Update entity %s: final state - installed=%s, latest=%s",
            self._device.device_name,
            self._attr_installed_version,
            self._attr_latest_version,
        )

        return True
    
    def _version_is_newer(self, latest_version: str, installed_version: str) -> bool:
        """Return True if latest_version is newer than installed_version."""
        try:
            return version.parse(str(latest_version)) > version.parse(
                str(installed_version),
            )
        except ImportError:
            # Fallback to simple string comparison if packaging is not available
            return str(latest_version) != str(installed_version)
        except Exception:
            _LOGGER.exception(
                "Error comparing versions %s and %s",
                latest_version,
                installed_version,
            )
            return False
    
    @property
    def release_summary(self) -> str | None:
        """Return summary of the latest release."""
        # TODO: Implement when API supports firmware update information
        return None
    
    @property
    def in_progress(self) -> bool:
        """Return whether an update is currently in progress."""
        # Check if there's a property indicating update status
        device = self.coordinator.get_device(self._device.device_id)
        if device:
            update_prop = device.properties.get("firmware_update_status")
            if update_prop and update_prop.value:
                return str(update_prop.value).lower() in ["updating", "downloading", "installing"]
        return False
    
    async def async_update(self) -> None:
        """Update the entity state from coordinator cache and check for firmware updates.

        This is called during polling by Home Assistant.
        Note: HA automatically calls async_write_ha_state() after async_update().
        """
        self._update_from_cache()
        
        # Check for firmware updates if we have an installed version
        if self._attr_installed_version:
            await self._check_firmware_update()
    
    async def _check_firmware_update(self) -> None:
        """Check for available firmware updates from Heiman API."""
        try:
            # Get firmware info from API
            firmware_info = await self.coordinator.api_client.async_get_device_firmware_info(
                device_id=self._device.device_id,
                product_id=self._device.product_id,
                device_name=self._device.device_name,
                current_version=self._attr_installed_version,
            )
            
            if not firmware_info:
                _LOGGER.debug(
                    "No firmware info returned for device %s",
                    self._device.device_id,
                )
                return
            
            # Store firmware upgrade info for later use
            self._firmware_upgrade_info = firmware_info
            
            # Extract latest version from firmware info
            latest_version = self._extract_latest_version(firmware_info)
            
            if latest_version and self._attr_installed_version:
                # Compare versions
                if self._version_is_newer(latest_version, self._attr_installed_version):
                    self._attr_latest_version = latest_version
                    
                    # Extract release notes if available
                    self._attr_release_summary = self._extract_release_notes(
                        firmware_info
                    )
                    
                    _LOGGER.info(
                        "Firmware update available for %s: %s -> %s",
                        self._device.device_name,
                        self._attr_installed_version,
                        latest_version,
                    )
                else:
                    # No update available
                    self._attr_latest_version = self._attr_installed_version
                    self._attr_release_summary = None
                    
        except Exception as err:  # noqa: BLE001
            _LOGGER.debug(
                "Failed to check firmware update for %s: %s",
                self._device.device_id,
                err,
            )
            # Don't raise exception - just log and continue with cached values
    
    def _extract_latest_version(self, firmware_info: dict[str, Any]) -> str | None:
        """Extract latest firmware version from firmware info response.
        
        Args:
            firmware_info: Firmware information from API
            
        Returns:
            Latest firmware version string or None
        """
        # Try different possible field names for latest version
        for key in ["latestVersion", "newVersion", "version", "targetVersion"]:
            if key in firmware_info and firmware_info[key]:
                return str(firmware_info[key])
        
        # Check in nested structure
        if "firmware" in firmware_info and isinstance(firmware_info["firmware"], dict):
            for key in ["version", "latestVersion", "newVersion"]:
                if key in firmware_info["firmware"] and firmware_info["firmware"][key]:
                    return str(firmware_info["firmware"][key])
        
        return None
    
    def _extract_release_notes(self, firmware_info: dict[str, Any]) -> str | None:
        """Extract release notes/description from firmware info.
        
        Args:
            firmware_info: Firmware information from API
            
        Returns:
            Release notes string or None
        """
        # Try different possible field names for release notes
        for key in [
            "description",
            "releaseNotes",
            "changeLog",
            "updateDescription",
            "remark",
        ]:
            if key in firmware_info and firmware_info[key]:
                return str(firmware_info[key])
        
        # Check in nested structure
        if "firmware" in firmware_info and isinstance(firmware_info["firmware"], dict):
            for key in ["description", "releaseNotes", "changeLog"]:
                if key in firmware_info["firmware"] and firmware_info["firmware"][key]:
                    return str(firmware_info["firmware"][key])
        
        return None
    
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator (MQTT push).

        This is called when the coordinator has new data (e.g., from MQTT).
        Updates entity state immediately without waiting for next poll.
        """
        _LOGGER.info(
            "_handle_coordinator_update called for %s",
            self._device.device_name,
        )
        if self._update_from_cache():
            # Write the new state to Home Assistant immediately
            _LOGGER.info(
                "Writing state for %s: installed=%s, latest=%s",
                self._device.device_name,
                self._attr_installed_version,
                self._attr_latest_version,
            )
            self.async_write_ha_state()
            _LOGGER.info(
                "State written for %s, notifying HA",
                self._device.device_name,
            )
    
    async def async_install(
        self,
        version: str | None = None,
        backup: bool = False,
    ) -> None:
        """Install a firmware update.
        
        Args:
            version: Specific version to install (optional)
            backup: Whether to create backup before update (not supported)
        """
        _LOGGER.info(
            "Starting firmware update for device %s (version: %s)",
            self._device.device_id,
            version or self._attr_latest_version,
        )
        
        self._attr_in_progress = True
        self._attr_update_percentage = 0
        self.async_write_ha_state()
        
        try:
            # Confirm firmware upgrade via API
            result = await self.coordinator.api_client.async_confirm_firmware_upgrade(
                device_id=self._device.device_id,
                product_id=self._device.product_id,
                device_name=self._device.device_name,
                current_version=self._attr_installed_version,
            )
            
            _LOGGER.info(
                "Firmware update initiated for device %s: %s",
                self._device.device_id,
                result,
            )
            
            # Update progress
            self._attr_update_percentage = 10
            self.async_write_ha_state()
            
            # Monitor update progress
            await self._monitor_update_progress()
            
        except Exception as err:  # noqa: BLE001
            _LOGGER.error(
                "Failed to install firmware update for %s: %s",
                self._device.device_id,
                err,
            )
            self._attr_in_progress = False
            self._attr_update_percentage = None
            self.async_write_ha_state()
            raise
    
    async def _monitor_update_progress(self) -> None:
        """Monitor firmware update progress."""
        max_attempts = 60  # Monitor for up to 10 minutes (10s intervals)
        attempt = 0
        
        while attempt < max_attempts:
            attempt += 1
            await asyncio.sleep(10)
            
            try:
                # Check upgrade history/progress
                history = await self.coordinator.api_client.async_get_firmware_upgrade_history(
                    device_id=self._device.device_id,
                )
                
                _LOGGER.info(
                    "Upgrade history for %s: %s",
                    self._device.device_id,
                    history,
                )
                
                if history:
                    progress = self._extract_update_progress(history)
                    status = self._extract_update_status(history)
                    
                    _LOGGER.info(
                        "Upgrade progress for %s: progress=%s, status=%s",
                        self._device.device_id,
                        progress,
                        status,
                    )
                    
                    if progress is not None:
                        self._attr_update_percentage = progress
                        self.async_write_ha_state()
                        
                        # If update completed or failed
                        status = self._extract_update_status(history)
                        if status == "completed":
                            _LOGGER.info(
                                "Firmware update completed for %s",
                                self._device.device_id,
                            )
                            self._attr_in_progress = False
                            self._attr_update_percentage = None
                            
                            # Refresh installed version
                            device = self.coordinator.get_device(self._device.device_id)
                            if device:
                                new_version = self._extract_firmware_version(device)
                                if new_version:
                                    self._attr_installed_version = new_version
                                    self._attr_latest_version = new_version
                            
                            self.async_write_ha_state()
                            return
                        elif status in ["failed", "error"]:
                            _LOGGER.error(
                                "Firmware update failed for %s",
                                self._device.device_id,
                            )
                            self._attr_in_progress = False
                            self._attr_update_percentage = None
                            self.async_write_ha_state()
                            return
            
            except Exception as err:  # noqa: BLE001
                _LOGGER.debug(
                    "Error checking update progress: %s",
                    err,
                )
        
        # Timeout
        _LOGGER.warning(
            "Firmware update monitoring timed out for %s",
            self._device.device_id,
        )
        self._attr_in_progress = False
        self._attr_update_percentage = None
        self.async_write_ha_state()
    
    def _extract_update_progress(self, history: dict[str, Any]) -> int | None:
        """Extract update progress percentage from history.
        
        Args:
            history: Upgrade history data
            
        Returns:
            Progress percentage (0-100) or None
        """
        # Try different field names
        for key in ["progress", "percentage", "upgradeProgress"]:
            if key in history:
                try:
                    return int(history[key])
                except (ValueError, TypeError):
                    pass
        
        # Check in nested structure
        if "task" in history and isinstance(history["task"], dict):
            for key in ["progress", "percentage"]:
                if key in history["task"]:
                    try:
                        return int(history["task"][key])
                    except (ValueError, TypeError):
                        pass
        
        return None
    
    def _extract_update_status(self, history: dict[str, Any]) -> str | None:
        """Extract update status from history.
        
        Args:
            history: Upgrade history data
            
        Returns:
            Status string or None
        """
        # Try different field names
        for key in ["status", "state", "upgradeStatus"]:
            if key in history:
                return str(history[key]).lower()
        
        # Check in nested structure
        if "task" in history and isinstance(history["task"], dict):
            for key in ["status", "state"]:
                if key in history["task"]:
                    return str(history["task"][key]).lower()
        
        return None
