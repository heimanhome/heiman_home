"""Number platform for Heiman integration."""

from __future__ import annotations

import logging
from typing import Any

from heimanconnect import DeviceProperty, HeimanDevice

from homeassistant import config_entries
from homeassistant.components.number import NumberEntity, NumberMode
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, ENTITY_ICONS
from .coordinator import HeimanDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: config_entries.ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Heiman numbers based on a config entry."""
    coordinator: HeimanDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    # Track existing entities to avoid duplicates
    existing_entities: set[str] = set()

    def _create_numbers_for_devices() -> None:
        """Create numbers for all devices and add new ones."""
        devices = coordinator.get_all_devices()
        new_numbers = []

        for device in devices:
            for property_id, prop in device.properties.items():
                # Must be writable
                if not prop.writable:
                    continue

                # Use entity field from DeviceProperty
                if hasattr(prop, "entity") and prop.entity == "number":
                    unique_id = f"{device.device_id}_{property_id}_number"
                    if unique_id not in existing_entities:
                        new_numbers.append(
                            HeimanNumberEntity(
                                coordinator=coordinator,
                                device=device,
                                property_identifier=property_id,
                            )
                        )
                        existing_entities.add(unique_id)

        if new_numbers:
            async_add_entities(new_numbers)

    # Initial setup
    _create_numbers_for_devices()

    # Listen for coordinator updates to add new devices dynamically
    entry.async_on_unload(coordinator.async_add_listener(_create_numbers_for_devices))


class HeimanNumberEntity(CoordinatorEntity[HeimanDataUpdateCoordinator], NumberEntity):
    """Representation of a Heiman number entity."""

    _attr_has_entity_name = True
    _attr_mode = NumberMode.BOX

    def __init__(
        self,
        coordinator: HeimanDataUpdateCoordinator,
        device: HeimanDevice,
        property_identifier: str,
    ) -> None:
        """Initialize the number entity.

        Args:
            coordinator: Data coordinator
            device: Heiman device
            property_identifier: Property identifier
        """
        super().__init__(coordinator)
        self._device = device
        self._property_identifier = property_identifier

        # Generate unique ID
        self._attr_unique_id = f"{device.device_id}_{property_identifier}_number"

        # Get property object
        prop = device.properties.get(property_identifier)

        # Set name
        self._attr_name = prop.name if prop else property_identifier

        # Get device info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.device_id)},
            name=device.device_name,
            manufacturer=device.manufacturer,
            model=device.model or device.product_id,
            sw_version=device.firmware_version,
            hw_version=device.hardware_version,
        )

        # Apply icon and setup number range
        if prop:
            self._apply_icon(property_identifier, prop)
            self._setup_number_range(prop)

        # Initialize current value from coordinator cache
        self._attr_native_value = None
        self._update_value_from_cache()

    def _setup_number_range(self, prop: DeviceProperty) -> None:
        """Setup number range and step based on property.

        Args:
            prop: Property object
        """
        # Set unit of measurement
        if prop.unit:
            self._attr_native_unit_of_measurement = prop.unit

        # Set default range based on data type
        if prop.data_type in ("int", "float", "double"):
            # Default ranges for common property types
            prop_lower = self._property_identifier.lower()

            # Temperature thresholds: -40 to 100°C
            if "temp" in prop_lower and "threshold" in prop_lower:
                self._attr_native_min_value = -40.0
                self._attr_native_max_value = 100.0
                self._attr_native_step = 0.5
            # Humidity thresholds: 0 to 100%
            elif "humidity" in prop_lower and "threshold" in prop_lower:
                self._attr_native_min_value = 0.0
                self._attr_native_max_value = 100.0
                self._attr_native_step = 1.0
            # Temperature comfort: -40 to 100°C
            elif "temp" in prop_lower and "comfort" in prop_lower:
                self._attr_native_min_value = -40.0
                self._attr_native_max_value = 100.0
                self._attr_native_step = 0.5
            # Humidity comfort: 0 to 100%
            elif "humidity" in prop_lower and "comfort" in prop_lower:
                self._attr_native_min_value = 0.0
                self._attr_native_max_value = 100.0
                self._attr_native_step = 1.0
            else:
                # Generic range for other numeric properties
                self._attr_native_min_value = 0.0
                self._attr_native_max_value = 1000.0
                self._attr_native_step = 1.0

    def _apply_icon(self, property_identifier: str, prop: DeviceProperty | None) -> None:
        """Apply icon based on property type.

        Args:
            property_identifier: Property identifier
            prop: Property object
        """
        # First try to get from ENTITY_ICONS (using original case)
        icons_config = ENTITY_ICONS.get("number", {})

        if property_identifier in icons_config:
            self._attr_icon = icons_config[property_identifier]
            return

        # If not found, try lowercase match
        prop_lower = property_identifier.lower()
        if prop_lower in icons_config:
            self._attr_icon = icons_config[prop_lower]
            return

        # Default number icon
        self._attr_icon = "mdi:numeric"

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not self.coordinator.last_update_success:
            return False

        device = self.coordinator.get_device(self._device.device_id)
        if not device:
            return False

        return device.online is True

    def _update_value_from_cache(self) -> bool:
        """Update value from coordinator cache (synchronous).

        Returns True if state was updated from cache, False if cache miss or no change.
        """
        device_id = self._device.device_id
        property_id = self._property_identifier

        if self.coordinator and hasattr(self.coordinator, "get_device_property"):
            cached_value = self.coordinator.get_device_property(device_id, property_id)

            if cached_value is not None:
                # Convert value to float for number entity
                try:
                    old_value = self._attr_native_value
                    self._attr_native_value = float(cached_value)

                    if self._attr_native_value != old_value:
                        return True
                except (ValueError, TypeError):
                    _LOGGER.warning(
                        "Failed to convert %s value to float: %s",
                        property_id,
                        cached_value,
                    )
        return False

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value.

        Args:
            value: New value to set
        """
        _LOGGER.info(
            "Setting %s to %s for device %s",
            self._property_identifier,
            value,
            self._device.device_id,
        )

        # Write property via MQTT client using async_write_property method
        if self.coordinator.mqtt_client:
            # Build device info for child device detection
            # Use raw_data if available, fallback to device attributes
            device_info = {}
            if hasattr(self._device, "raw_data") and self._device.raw_data:
                device_info = {
                    "deviceType": self._device.raw_data.get("deviceType"),
                    "parentId": self._device.raw_data.get("parentId"),
                }
            else:
                device_info = {
                    "deviceType": getattr(self._device, "device_type", None),
                    "parentId": getattr(self._device, "parent_id", None),
                }

            await self.coordinator.mqtt_client.async_write_property(
                device_id=self._device.device_id,
                product_id=self._device.product_id,
                property_identifiers=[self._property_identifier],
                values={self._property_identifier: value},
                device_info=device_info,
            )

        # Update value immediately for better UX
        self._attr_native_value = value
        self.async_write_ha_state()

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        attributes = {}

        device = self.coordinator.get_device(self._device.device_id)
        if device:
            prop = device.properties.get(self._property_identifier)
            if prop:
                if prop.unit:
                    attributes["unit"] = prop.unit
                if prop.data_type:
                    attributes["data_type"] = prop.data_type
                attributes["raw_value"] = prop.value

        return attributes
