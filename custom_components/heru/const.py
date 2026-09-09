"""Constants file"""

from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.helpers.entity import EntityCategory

NAME = "HERU"
DOMAIN = "heru"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.1.0"

# Icon
ICON_FAN = "mdi:fan"
ICON_HEAT_WAVE = "mdi:heat-wave"
ICON_EXCHANGE = "mdi:swap-horizontal"
ICON_ALARM = "mdi:bell"
ICON_SWITCH = "mdi:electric-switch"
ICON_THERMOMETER = "mdi:thermometer"
ICON_SWITCH = "mdi:toggle-switch-variant"
ICON_PLAY = "mdi:play-circle-outline"
ICON_TIME_SYNC = "mdi:timer-sync"
ICON_CALENDAR = "mdi:calendar"
ICON_THERMOSTAT = "mdi:home-thermometer"
ICON_START = "mdi:ray-start-arrow"
ICON_COOLING = "mdi:snowflake"
ICON_THERMOMETER_LINES = "mdi:thermometer-lines"
ICON_AIR_PURIFIER = "mdi:air-purifier"

# Platforms
SENSOR = Platform.SENSOR
SWITCH = Platform.SWITCH
BUTTON = Platform.BUTTON
NUMBER = Platform.NUMBER
SELECT = Platform.SELECT
CLIMATE = Platform.CLIMATE
BINARY_SENSOR = Platform.BINARY_SENSOR
FAN = Platform.FAN
PLATFORMS = [SENSOR, SWITCH, BUTTON, CLIMATE, NUMBER, BINARY_SENSOR, FAN]
# PLATFORMS = [SWITCH, SENSOR, BUTTON, NUMBER, SELECT]

# Modbus
DEFAULT_SLAVE = 1
REGISTER_HOLDING = "holding"
REGISTER_COILS = "coils"

# Configuration and options
CONF_HOST_NAME = "host_name"
CONF_HOST_PORT = "host_port"
CONF_DEVICE_NAME = "device_name"
CONF_FAN_CONTROL = "fan_control"

# Modbus register types
INPUT_REGISTERS = "input_registers"
INPUT_REGISTERS_BINARY = "input_registers_binary"
DISCRETE_INPUTS = "discrete_inputs"
HOLDING_REGISTERS = "holding_registers"
COIL = "coil"

#  Button class types
BUTTON_CLASS_START = "button_class_start"
BUTTON_CLASS_SET_TIME = "button_class_set_time"


HERU_SENSORS = [
    {
        "name": "Outdoor temperature",
        "modbus_address": "3x00002",
        "scale": 0.1,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Temperature of the fresh air drawn in from outside, before heat recovery.",
    },
    {
        "name": "Supply air temperature",
        "modbus_address": "3x00003",
        "scale": 0.1,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Temperature of the air supplied into the building, after heat recovery and any heater/cooler.",
    },
    {
        "name": "Extract air temperature",
        "modbus_address": "3x00004",
        "scale": 0.1,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Temperature of the air extracted from inside the building, before it enters the heat exchanger.",
    },
    {
        "name": "Exhaust air temperature",
        "modbus_address": "3x00005",
        "scale": 0.1,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Temperature of the air exhausted to the outside, after passing through the heat exchanger.",
    },
    {
        "name": "Heat recovery temperature",
        "modbus_address": "3x00007",
        "scale": 0.1,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Temperature measured on the heat recovery wheel/rotor.",
    },
    {
        "name": "Room temperature",
        "modbus_address": "3x00008",
        "scale": 0.1,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "entity_registry_enabled_default": False,
        "description": "Temperature measured by an optional room sensor. Only meaningful if a room sensor is installed and wired.",
    },
    {
        "name": "Current exhaust fan power",
        "modbus_address": "3x00026",
        "scale": 1,
        "icon": ICON_FAN,
        "unit_of_measurement": "%",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Current exhaust fan power as a percentage of maximum.",
    },
    {
        "name": "Current exhaust fan speed",
        "modbus_address": "3x00028",
        "scale": 1,
        "icon": ICON_FAN,
        "unit_of_measurement": "rpm",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Current exhaust fan rotational speed.",
    },
    {
        "name": "Current exhaust fan control voltage",
        "modbus_address": "3x00033",
        "scale": 0.1,
        "icon": ICON_FAN,
        "unit_of_measurement": "V",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Control voltage currently applied to the exhaust EC fan (0-10V control signal).",
    },
    {
        "name": "Current heating power",
        "modbus_address": "3x00029",
        "scale": 0.3921568627,
        "precision": 2,
        "icon": ICON_HEAT_WAVE,
        "unit_of_measurement": "%",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Current output power of the heater (electric or water), converted from its raw 0-255 scale to a percentage.",
    },
    {
        "name": "Current cooling power",
        "modbus_address": "3x00031",
        "scale": 0.3921568627,
        "precision": 2,
        "icon": ICON_HEAT_WAVE,
        "unit_of_measurement": "%",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Current output power of the cooler, converted from its raw 0-255 scale to a percentage.",
    },
    {
        "name": "Current supply fan power",
        "modbus_address": "3x00025",
        "scale": 1,
        "icon": ICON_FAN,
        "unit_of_measurement": "%",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Current supply fan power as a percentage of maximum.",
    },
    {
        "name": "Current supply fan speed",
        "modbus_address": "3x00027",
        "scale": 1,
        "icon": ICON_FAN,
        "unit_of_measurement": "rpm",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Current supply fan rotational speed.",
    },
    {
        "name": "Current supply fan control voltage",
        "modbus_address": "3x00032",
        "scale": 0.1,
        "icon": ICON_FAN,
        "unit_of_measurement": "V",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Control voltage currently applied to the supply EC fan (0-10V control signal).",
    },
    {
        "name": "Current heat/cold recovery power",
        "modbus_address": "3x00030",
        "scale": 0.3921568627,
        "precision": 2,
        "icon": ICON_EXCHANGE,
        "unit_of_measurement": "%",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Current output power of the heat recovery wheel, converted from its raw 0-255 scale to a percentage.",
    },
    {
        "name": "Filter timer alarm",
        "modbus_address": "1x00025",
        "scale": None,
        "icon": ICON_ALARM,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the filter change timer has expired and the filters need to be replaced.",
    },
    {
        "name": "Exhaust fan alarm",
        "modbus_address": "1x00022",
        "scale": None,
        "icon": ICON_ALARM,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the exhaust fan has failed or is not running as expected.",
    },
    {
        "name": "Boost input",
        "modbus_address": "1x00002",
        "scale": None,
        "icon": ICON_SWITCH,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "description": "Reflects the state of the external boost input/switch wired to the unit.",
    },
    {
        "name": "Overpressure input",
        "modbus_address": "1x00003",
        "scale": None,
        "icon": ICON_SWITCH,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "description": "Reflects the state of the external overpressure input/switch wired to the unit.",
    },
    {
        "name": "Fire alarm",
        "modbus_address": "1x00010",
        "scale": None,
        "icon": ICON_ALARM,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the unit's fire alarm has triggered (fans stop, dampers close).",
    },
    {
        "name": "Rotor alarm",
        "modbus_address": "1x00011",
        "scale": None,
        "icon": ICON_ALARM,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the heat recovery rotor/wheel has failed or stopped turning.",
    },
    {
        "name": "Supply fan alarm",
        "modbus_address": "1x00021",
        "scale": None,
        "icon": ICON_ALARM,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the supply fan has failed or is not running as expected.",
    },
    {
        "name": "Current supply fan step",
        "modbus_address": "3x00023",
        "scale": None,
        "icon": ICON_FAN,
        "unit_of_measurement": None,
        "device_class": SensorDeviceClass.ENUM,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "options": ["Off", "Minimum", "Standard", "Moderate", "Maximum"],
        "description": "Current supply fan step, as set by the user or the week timer.",
    },
    {
        "name": "Current exhaust fan step",
        "modbus_address": "3x00024",
        "scale": None,
        "icon": ICON_FAN,
        "unit_of_measurement": None,
        "device_class": SensorDeviceClass.ENUM,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "options": ["Off", "Minimum", "Standard", "Moderate", "Maximum"],
        "description": "Current exhaust fan step, as set by the user or the week timer.",
    },
    {
        "name": "Current fan speed",
        "modbus_address": "3x00022",
        "scale": None,
        "icon": ICON_FAN,
        "unit_of_measurement": None,
        "device_class": SensorDeviceClass.ENUM,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "options": ["Off", "Minimum", "Standard", "Moderate", "Maximum"],
        "description": "Overall current fan speed level (combined supply/exhaust), as set by the user or the week timer.",
    },
    {
        "name": "Supply pressure",
        "modbus_address": "3x00012",
        "scale": 0.1,
        "icon": "mdi:gauge",
        "unit_of_measurement": "Pa",
        "device_class": SensorDeviceClass.PRESSURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": INPUT_REGISTERS,
        "entity_registry_enabled_default": False,
        "description": "Static pressure measured in the supply air duct. Only valid if a supply pressure sensor is installed.",
    },
    {
        "name": "Exhaust pressure",
        "modbus_address": "3x00013",
        "scale": 0.1,
        "icon": "mdi:gauge",
        "unit_of_measurement": "Pa",
        "device_class": SensorDeviceClass.PRESSURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": INPUT_REGISTERS,
        "entity_registry_enabled_default": False,
        "description": "Static pressure measured in the exhaust air duct. Only valid if an exhaust pressure sensor is installed.",
    },
    {
        "name": "Relative humidity",
        "modbus_address": "3x00014",
        "scale": 0.1,
        "icon": "mdi:water-percent",
        "unit_of_measurement": "%",
        "device_class": SensorDeviceClass.HUMIDITY,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "entity_registry_enabled_default": False,
        "description": "Relative humidity measured in the extract air. Only valid if an RH sensor is installed.",
    },
    {
        "name": "Carbon dioxide",
        "modbus_address": "3x00015",
        "scale": 1,
        "icon": "mdi:molecule-co2",
        "unit_of_measurement": "ppm",
        "device_class": SensorDeviceClass.CO2,
        "state_class": SensorStateClass.MEASUREMENT,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "entity_registry_enabled_default": False,
        "description": "CO2 concentration measured in the extract air. Only valid if a CO2 sensor is installed.",
    },
    {
        "name": "Filter days left",
        "modbus_address": "3x00020",
        "scale": 1,
        "icon": ICON_CALENDAR,
        "unit_of_measurement": "days",
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": INPUT_REGISTERS,
        "description": "Number of days remaining until the next scheduled filter change.",
    },
    {
        "name": "Startup 1st phase",
        "modbus_address": "1x00028",
        "scale": None,
        "icon": ICON_START,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active during the unit's first startup phase, while the supply fan is still stopped.",
    },
    {
        "name": "Startup 2nd phase",
        "modbus_address": "1x00029",
        "scale": None,
        "icon": ICON_START,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active during the unit's second startup phase, before heating or cooling is allowed to start.",
    },
    {
        "name": "Cooling",
        "modbus_address": "1x00032",
        "scale": None,
        "icon": ICON_COOLING,
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "description": "Active while the unit's cooler is actively cooling the supply air.",
    },
    {
        "name": "Temperature regulation mode",
        "modbus_address": "4x00012",
        "scale": None,
        "icon": ICON_THERMOMETER_LINES,
        "unit_of_measurement": None,
        "device_class": SensorDeviceClass.ENUM,
        "state_class": None,
        "entity_category": None,
        "register_type": HOLDING_REGISTERS,
        "options": ["Supply", "Extract", "Room", "Extract S/W", "Room S/W"],
        "description": "Which air temperature the unit's control loop targets: Supply, Extract, Room, or a Summer/Winter changeover variant.",
    },
]


HERU_BINARY_SENSORS = [
    {
        "name": "Fire alarm switch",
        "modbus_address": "1x00001",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Raw state of the external fire alarm switch input wired to the unit (separate from the resulting 'Fire alarm' state).",
    },
    {
        "name": "Aux switch",
        "modbus_address": "1x00004",
        "icon": ICON_SWITCH,
        "device_class": None,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "description": "Reflects the state of the auxiliary external input wired to the unit.",
    },
    {
        "name": "Freeze alarm",
        "modbus_address": "1x00013",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the unit has detected a risk of the heat exchanger or water coil freezing.",
    },
    {
        "name": "Low supply temperature alarm",
        "modbus_address": "1x00014",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the supply air temperature has dropped below the configured minimum.",
    },
    {
        "name": "Low rotor temperature alarm",
        "modbus_address": "1x00015",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the heat recovery rotor temperature is dangerously low.",
    },
    {
        "name": "Temperature sensor open circuit alarm",
        "modbus_address": "1x00018",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when one of the unit's temperature sensors has an open-circuit fault (per-sensor detail is a bit field in register 3x00018).",
    },
    {
        "name": "Temperature sensor short circuit alarm",
        "modbus_address": "1x00019",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when one of the unit's temperature sensors has a short-circuit fault (per-sensor detail is a bit field in register 3x00019).",
    },
    {
        "name": "Pulser alarm",
        "modbus_address": "1x00020",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the rotor pulse sensor failed to detect movement, i.e. the heat recovery wheel does not appear to be turning.",
    },
    {
        "name": "Supply filter alarm",
        "modbus_address": "1x00023",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the supply air filter needs replacing.",
    },
    {
        "name": "Exhaust filter alarm",
        "modbus_address": "1x00024",
        "icon": ICON_ALARM,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active when the exhaust air filter needs replacing.",
    },
    {
        "name": "Freeze protection B level",
        "modbus_address": "1x00026",
        "icon": ICON_COOLING,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active at the higher freeze-protection threshold: the water valve opens fully to prevent the coil from freezing.",
    },
    {
        "name": "Freeze protection A level",
        "modbus_address": "1x00027",
        "icon": ICON_COOLING,
        "device_class": BinarySensorDeviceClass.PROBLEM,
        "entity_category": EntityCategory.DIAGNOSTIC,
        "register_type": DISCRETE_INPUTS,
        "description": "Active at the lower freeze-protection threshold: the unit shuts down but keeps the water valve open.",
    },
    {
        "name": "Heating",
        "modbus_address": "1x00030",
        "icon": ICON_HEAT_WAVE,
        "device_class": BinarySensorDeviceClass.RUNNING,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "description": "Active while the unit's heater is actively heating the supply air.",
    },
    {
        "name": "Recovering heat/cold",
        "modbus_address": "1x00031",
        "icon": ICON_EXCHANGE,
        "device_class": BinarySensorDeviceClass.RUNNING,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "description": "Active while the heat recovery wheel is actively transferring heat or cold between the air streams.",
    },
    {
        "name": "CO2 boost",
        "modbus_address": "1x00033",
        "icon": ICON_AIR_PURIFIER,
        "device_class": BinarySensorDeviceClass.RUNNING,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "entity_registry_enabled_default": False,
        "description": "Active when fan speed has been automatically boosted due to a high CO2 reading. Only meaningful if a CO2 sensor is installed.",
    },
    {
        "name": "RH boost",
        "modbus_address": "1x00034",
        "icon": ICON_AIR_PURIFIER,
        "device_class": BinarySensorDeviceClass.RUNNING,
        "entity_category": None,
        "register_type": DISCRETE_INPUTS,
        "entity_registry_enabled_default": False,
        "description": "Active when fan speed has been automatically boosted due to a high humidity reading. Only meaningful if an RH sensor is installed.",
    },
]


HERU_NUMBERS = [
    {
        "name": "Night cooling indoor-outdoor diff. limit",
        "modbus_address": "4x00020",
        "scale": 0.1,
        "min_value": 1,
        "max_value": 10,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "description": "Minimum temperature difference between extract air and outdoor air required for night cooling to activate.",
    },
    {
        "name": "Night cooling exhaust high limit",
        "modbus_address": "4x00021",
        "scale": 1,
        "min_value": 18,
        "max_value": 24,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "description": "Extract air temperature above which night cooling activates.",
    },
    {
        "name": "Night cooling exhaust low limit",
        "modbus_address": "4x00022",
        "scale": 1,
        "min_value": 19,
        "max_value": 26,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "description": "Extract air temperature below which night cooling deactivates.",
    },
    {
        "name": "Setpoint max limit (Comfort)",
        "modbus_address": "4x00048",
        "scale": 1,
        "min_value": 15,
        "max_value": 40,
        "icon": ICON_THERMOMETER,
        "unit_of_measurement": "°C",
        "description": "Maximum temperature the Comfort setpoint can be set to.",
    },
]


HERU_BUTTONS = [
    {
        "name": "Clear Alarms",
        "modbus_address": "0x00005",
        "icon": ICON_PLAY,
        "entity_class": BUTTON_CLASS_START,
        "description": "Clears all currently active alarms on the unit.",
    },
    {
        "name": "Reset filter timer",
        "modbus_address": "0x00006",
        "icon": ICON_PLAY,
        "entity_class": BUTTON_CLASS_START,
        "description": "Resets the filter change countdown timer back to its full configured period.",
    },
    {
        "name": "Sync date and time",
        "modbus_address": "4x00400",
        "icon": ICON_TIME_SYNC,
        "entity_class": BUTTON_CLASS_SET_TIME,
        "description": "Writes Home Assistant's current date and time to the unit's clock registers (4x00400-4x00405).",
    },
]


HERU_SWITCHES = [
    {
        "name": "Power",
        "modbus_address": "0x00001",
        "icon": ICON_SWITCH,
        "register_type": COIL,
        "description": "Turns the whole unit on or off.",
    },
    {
        "name": "Overpressure mode",
        "modbus_address": "0x00002",
        "icon": ICON_SWITCH,
        "register_type": COIL,
        "description": "Manually activates overpressure mode (e.g. for use with a fireplace), boosting the supply fan relative to the exhaust fan.",
    },
    {
        "name": "Boost mode",
        "modbus_address": "0x00003",
        "icon": ICON_SWITCH,
        "register_type": COIL,
        "description": "Manually activates boost mode, temporarily increasing fan speed.",
    },
    {
        "name": "Away mode",
        "modbus_address": "0x00004",
        "icon": ICON_SWITCH,
        "register_type": COIL,
        "description": "Manually activates away mode, reducing fan speed while nobody is home.",
    },
    {
        "name": "Preheater enabled",
        "modbus_address": "4x00064",
        "icon": ICON_SWITCH,
        "register_type": HOLDING_REGISTERS,
        "description": "Enables or disables the electric preheater (frost protection heating element ahead of the heat exchanger).",
    },
    {
        "name": "Heater enabled",
        "modbus_address": "4x00067",
        "icon": ICON_SWITCH,
        "register_type": HOLDING_REGISTERS,
        "description": "Enables or disables the main heater used to reach the temperature setpoint.",
    },
    {
        "name": "Night cooling enabled",
        "modbus_address": "4x00019",
        "icon": ICON_COOLING,
        "register_type": HOLDING_REGISTERS,
        "description": "Enables or disables automatic night cooling (using cool outdoor air overnight to pre-cool the building).",
    },
    {
        "name": "Cooler enabled",
        "modbus_address": "4x00069",
        "icon": ICON_COOLING,
        "register_type": HOLDING_REGISTERS,
        "description": "Enables or disables the cooler.",
    },
]


HERU_CLIMATES = [
    {
        "name": "Comfort",
        "modbus_address": "4x00002",
        "icon": ICON_THERMOSTAT,
        "description": "Main temperature setpoint used by the unit's control loop (the actual target sensor depends on the configured regulation mode: supply, extract or room).",
    }
]

HERU_FANS = [
    {
        "name": "Supply fan",
        "modbus_address": "4x00003",
        "modbus_address_get": "3x00025",
        "icon": ICON_FAN,
        "description": "Directly overrides the supply fan's EC speed (0-100%), bypassing the unit's built-in control logic. Advanced/manual override, see the Fan Control warning in the README.",
    },
    {
        "name": "Exhaust fan",
        "modbus_address": "4x00004",
        "modbus_address_get": "3x00026",
        "icon": ICON_FAN,
        "description": "Directly overrides the exhaust fan's EC speed (0-100%), bypassing the unit's built-in control logic. Advanced/manual override, see the Fan Control warning in the README.",
    },
]
