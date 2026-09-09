"""Fan"""
import logging
from custom_components.heru.entity import HeruEntity

from homeassistant.components.fan import (
    FanEntity,
    FanEntityFeature,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType


from .const import (
    DOMAIN,
    HERU_FANS,
    CONF_FAN_CONTROL,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigType,
    async_add_devices: AddEntitiesCallback,
) -> None:
    """Setup climate platform."""
    _LOGGER.debug("Heru.fan.py")
    coordinator = hass.data[DOMAIN]["coordinator"]

    fan_control_enabled = entry.data.get(CONF_FAN_CONTROL, False)
    _LOGGER.debug("Fan control enabled: %s", fan_control_enabled)

    if fan_control_enabled:
        fans = []
        for fan in HERU_FANS:
            fans.append(HeruFan(coordinator, fan, entry))
        async_add_devices(fans)

class HeruFan(HeruEntity, FanEntity):
    """Representation of a modbus controlled Heru Fan."""

    # https://developers.home-assistant.io/docs/core/entity/fan/

    def __init__(self, coordinator, idx, config_entry) -> None:
        """Initialize the modbus fan."""
        _LOGGER.debug("HeruFan.__init__()")
        super().__init__(coordinator, idx, config_entry)
        self.coordinator = coordinator
        self.idx = idx
        self.modbus_address_set = self.idx["modbus_address"]
        self.modbus_address_get = self.idx["modbus_address_get"]

        self._attr_percentage = self._get_percentage()
        self._last_on_percentage = self._attr_percentage or 50
        self._attr_supported_features = (
            FanEntityFeature.SET_SPEED
            | FanEntityFeature.TURN_ON
            | FanEntityFeature.TURN_OFF
        )
        self._enable_turn_on_off_backwards_compatibility = False

    def _get_percentage(self):
        """Return the current speed percentage of the fan."""
        return self.coordinator.get_register(self.modbus_address_get)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        _LOGGER.debug("HeruFan._handle_coordinator_update()")
        self._attr_percentage = self._get_percentage()

        _LOGGER.debug(
            "update %s: %d",
            self._attr_name,
            self._attr_percentage,
        )
        self.async_write_ha_state()

    async def async_set_percentage(self, percentage: int) -> None:
        """Set the speed percentage of the fan."""
        await self.coordinator.write_register_by_address(self.modbus_address_set, percentage)

        # Update directly after writing, the actual value will be set on the next update from the coordinator
        self._attr_percentage = percentage
        if percentage:
            self._last_on_percentage = percentage
        _LOGGER.debug(
            "set %s: %d",
            self._attr_name,
            self._attr_percentage,
        )
        self.async_write_ha_state()

    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs) -> None:
        """Turn on the fan, restoring the last used speed if none is given."""
        _LOGGER.debug("HeruFan.async_turn_on()")
        await self.async_set_percentage(percentage if percentage is not None else self._last_on_percentage)

    async def async_turn_off(self, **kwargs) -> None:
        """Turn off the fan by setting its speed to 0%."""
        _LOGGER.debug("HeruFan.async_turn_off()")
        await self.async_set_percentage(0)
