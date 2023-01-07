import logging
from dataclasses import dataclass
from dataclasses import field

from homeassistant.components.sensor import (
    SensorDeviceClass,
)

"""Constants for the Porsche Connect integration."""

DOMAIN = "porscheconnect"
LOGGER = logging.getLogger(__package__)
DEFAULT_SCAN_INTERVAL = 660
HA_SENSOR = "sensor"
HA_SWITCH = "switch"
HA_LOCK = "lock"
HA_NUMBER = "number"
HA_DEVICE_TRACKER = "device_tracker"
HA_BINARY_SENSOR = "binary_sensor"
PORSCHE_COMPONENTS = [
    HA_SENSOR,
    HA_DEVICE_TRACKER,
    HA_BINARY_SENSOR,
    HA_SWITCH,
    HA_LOCK,
]

NAME = "porscheconnect"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.8"
ISSUE_URL = "https://github.com/cjne/ha-porscheconnect/issues"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""


@dataclass
class SensorMeta:
    name: str
    key: str
    icon: str = None
    device_class: str = None
    default_enabled: bool = True
    attributes: list = field(default_factory=list)


@dataclass
class BinarySensorMeta:
    name: str
    key: str
    icon: str = None
    device_class: str = None
    default_enabled: bool = True
    attributes: list = field(default_factory=list)


@dataclass
class SwitchMeta:
    name: str
    key: str
    on_action: str
    off_action: str
    icon: str = None
    device_class: str = None
    default_enabled: bool = True
    attributes: list = field(default_factory=list)


@dataclass
class LockMeta:
    name: str
    key: str
    icon: str = None
    device_class: str = None
    default_enabled: bool = True
    attributes: list = field(default_factory=list)


@dataclass
class NumberMeta:
    name: str
    key: str
    icon: str = None
    device_class: str = None
    default_enabled: bool = True
    attributes: list = field(default_factory=list)


@dataclass
class SensorAttr:
    name: str
    key: str


DATA_MAP = [
    SensorMeta(
        "mileage sensor",
        "mileage",
        "mdi:counter",
        attributes=[SensorAttr("oil level", "oilLevel")],
    ),
    SensorMeta(
        "battery sensor", "batteryLevel", "mdi:battery", SensorDeviceClass.BATTERY
    ),
    SensorMeta("fuel sensor", "fuelLevel", "mdi:gauge"),
    SensorMeta(
        "range sensor",
        "remainingRanges.electricalRange.distance",
        "mdi:gauge",
    ),
    SensorMeta(
        "range sensor",
        "remainingRanges.conventionalRange.distance",
        "mdi:gauge",
    ),
    SensorMeta(
        "charging profile sensor",
        "chargingProfiles.currentProfileId",
        "mdi:battery-charging",
        attributes=[SensorAttr("profiles", "chargingProfilesDict")],
    ),
    SwitchMeta(
        "climate",
        "directClimatisation.climatisationState",
        "climate-on",
        "climate-off",
        "mdi:thermometer",
    ),
    SwitchMeta(
        "direct charge",
        "directCharge.isActive",
        "directcharge-on",
        "directcharge-off",
        "mdi:ev-station",
    ),
    BinarySensorMeta("parking brake", "parkingBrake", "mdi:lock"),
    SensorMeta("doors", "overallOpenStatus", "mdi:lock"),
    SensorMeta(
        "charger sensor",
        "chargingStatus",
        "mdi:ev-station",
        attributes=[
            SensorAttr("plug state", "batteryChargeStatus.plugState"),
            SensorAttr("charging state", "batteryChargeStatus.chargingState"),
            SensorAttr("lock state", "batteryChargeStatus.lockState"),
            SensorAttr("charging mode", "batteryChargeStatus.chargingMode"),
            SensorAttr(
                "remaining charge time to 100%",
                "batteryChargeStatus.remainingChargeTimeUntil100PercentInMinutes",
            ),
            SensorAttr("charging power", "batteryChargeStatus.chargingPower"),
        ],
    ),
    LockMeta("doorlock", "doors.overallLockStatus", "mdi:lock"),
    NumberMeta("charging level", "chargingProfilesDict", "mdi:battery-charging"),
]


DEVICE_CLASSES = {
    "batteryLevel": SensorDeviceClass.BATTERY,
}

DEVICE_NAMES = {
    "mileage": "mileage sensor",
    "batteryLevel": "battery sensor",
    "fuelLevel": "fuel sensor",
    "oilLevel": "oil sensor",
    "remainingRanges.conventionalRange.distance": "range sensor",
    "remainingRanges.electricalRange.distance": "range sensor",
    "chargingStatus": "charger sensor",
    "chargingProfiles.currentProfileId": "charging profile",
    "directClimatisation.climatisationState": "climatisation",
    "directCharge.isActive": "direct charge",
    "doors.overallLockStatus": "door lock",
    "chargingProfilesDict": "charging level",
}

ICONS = {
    "battery sensor": "mdi:battery",
    "range sensor": "mdi:gauge",
    "mileage sensor": "mdi:counter",
    "parking brake sensor": "mdi:car-brake-parking",
    "charger sensor": "mdi:ev-station",
    "charger switch": "mdi:battery-charging",
    "update switch": "mdi:update",
    "maxrange switch": "mdi:gauge-full",
    "temperature sensor": "mdi:thermometer",
    "location tracker": "mdi:crosshairs-gps",
    "charging rate sensor": "mdi:speedometer",
    "sentry mode switch": "mdi:shield-car",
}
