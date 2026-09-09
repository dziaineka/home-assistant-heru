"""Binary Sensor platform for HERU."""
import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from pymodbus.client.mixin import ModbusClientMixin

from .const import (
    DISCRETE_INPUTS,
    DOMAIN,
    HERU_BINARY_SENSORS,
)
from .entity import HeruEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry, async_add_devices: AddEntitiesCallback
):
    """Setup binary sensor platform."""
    _LOGGER.debug("HeruBinarySensor.binary_sensor.py")
    coordinator = hass.data[DOMAIN]["coordinator"]

    binary_sensors = []
    for sensor in HERU_BINARY_SENSORS:
        binary_sensors.append(HeruBinarySensor(coordinator, sensor, entry))
    binary_sensors.append(HeruSncConditionsMetSensor(coordinator, entry))

    if binary_sensors:
        async_add_devices(binary_sensors)


class HeruBinarySensor(HeruEntity, BinarySensorEntity):
    """HERU binary sensor class for discrete inputs."""

    def __init__(self, coordinator: CoordinatorEntity, idx, config_entry):
        _LOGGER.debug("HeruBinarySensor.__init__()")
        super().__init__(coordinator, idx, config_entry)
        self.coordinator = coordinator
        self.idx = idx
        self.name = self.idx["name"]
        self.modbus_address = self.idx["modbus_address"]
        self.register_type = self.idx["register_type"]
        self._attr_device_class = self.idx.get("device_class", None)
        self._attr_entity_category = self.idx["entity_category"]

        if "entity_registry_enabled_default" in self.idx:
            self._attr_entity_registry_enabled_default = self.idx["entity_registry_enabled_default"]

        self._attr_is_on = self._get_value()

    def _get_value(self):
        """Get the value from the coordinator"""
        value = self.coordinator.get_register(self.modbus_address)
        return bool(value)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        _LOGGER.debug("HeruBinarySensor._handle_coordinator_update()")
        self._attr_is_on = self._get_value()
        _LOGGER.debug(
            "%s: %s",
            self._attr_name,
            self._attr_is_on,
        )
        self.async_write_ha_state()


class HeruSncConditionsMetSensor(HeruEntity, BinarySensorEntity):
    """Whether SNC / Night cooling ("Sommarkyla") activation conditions are currently met.

    This does not read a single Modbus register - it's calculated from the same
    temperatures and limits the unit's own firmware uses to decide whether to engage
    SNC. It reflects only the *activation* condition, not the (different) deactivation
    hysteresis, and does not by itself mean SNC is actually running - it also needs
    "Night cooling enabled" (4x00016) to be on.
    """

    def __init__(self, coordinator: CoordinatorEntity, config_entry):
        _LOGGER.debug("HeruSncConditionsMetSensor.__init__()")
        idx = {
            "name": "SNC conditions met",
            "icon": "mdi:weather-night",
            "modbus_address": "snc_conditions_met",
            "description": (
                "True when outdoor and extract air temperatures currently satisfy SNC / "
                "Night cooling's activation thresholds: extract air temperature above the "
                "exhaust high limit (4x00015) AND outdoor temperature below extract "
                "temperature minus the indoor-outdoor diff limit (4x00013). SNC also needs "
                "'Night cooling enabled' (4x00016) switched on to actually engage. "
                "Deactivation uses separate, lower hysteresis thresholds (exhaust low limit "
                "4x00014 / diff + 1.0C) which are not modeled by this sensor."
            ),
        }
        super().__init__(coordinator, idx, config_entry)
        self.coordinator = coordinator
        self._attr_device_class = None
        self._attr_entity_category = None
        self._update_state()

    def _read_values(self):
        """Read and convert the registers the SNC activation condition depends on."""
        outdoor_raw = self.coordinator.get_register("3x00002")
        extract_raw = self.coordinator.get_register("3x00004")
        exhaust_high = self.coordinator.get_register("4x00015")
        diff_limit_raw = self.coordinator.get_register("4x00013")
        snc_enable = self.coordinator.get_register("4x00016")

        if None in (outdoor_raw, extract_raw, exhaust_high, diff_limit_raw):
            return None

        outdoor = ModbusClientMixin.convert_from_registers([outdoor_raw], ModbusClientMixin.DATATYPE.INT16) * 0.1
        extract = ModbusClientMixin.convert_from_registers([extract_raw], ModbusClientMixin.DATATYPE.INT16) * 0.1
        diff_limit = diff_limit_raw * 0.1

        return {
            "outdoor_temperature": round(outdoor, 1),
            "extract_temperature": round(extract, 1),
            "exhaust_high_limit": exhaust_high,
            "indoor_outdoor_diff_limit": round(diff_limit, 1),
            "outdoor_threshold": round(extract - diff_limit, 1),
            "extract_above_exhaust_high": extract > exhaust_high,
            "outdoor_below_threshold": outdoor < (extract - diff_limit),
            "snc_enabled": bool(snc_enable),
        }

    def _update_state(self):
        """Recompute is_on and the diagnostic attributes from the latest coordinator data."""
        values = self._read_values()
        attributes = {
            "description": self.idx["description"],
            "modbus_address": self.idx["modbus_address"],
        }
        if values is None:
            self._attr_is_on = None
        else:
            self._attr_is_on = values["extract_above_exhaust_high"] and values["outdoor_below_threshold"]
            attributes.update(values)
        self._attr_extra_state_attributes = attributes

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        _LOGGER.debug("HeruSncConditionsMetSensor._handle_coordinator_update()")
        self._update_state()
        _LOGGER.debug("%s: %s", self._attr_name, self._attr_is_on)
        self.async_write_ha_state()
