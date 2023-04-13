from pydantic import BaseModel
from typing import Optional

class Devices(BaseModel):
    id: int
    status: bool

class DevicesPut(BaseModel):
    status: Optional[bool]

class DeviceDetails(BaseModel):
    id: int
    device_id: int
    name: str
    room: str
    type: str

class DevicesDetailsPut(BaseModel):
    device_id: Optional[int]
    name: Optional[str]
    room: Optional[str]
    type: Optional[str]

class Fan(BaseModel):
    id: int
    status: bool
    speed: int

class FanPut(BaseModel):
    status: Optional[bool]
    speed: Optional[int]

class FanDetails(BaseModel):
    id: int
    device_id: int
    name: str
    room: str
    type: str

class FanDetailsPut(BaseModel):
    device_id: Optional[int]
    name: Optional[str]
    room: Optional[str]
    type: Optional[str]

class Led(BaseModel):
    id: int
    brightness: str
    status: bool
    R: str
    G: str
    B: str

class LedPut(BaseModel):
    brightness: Optional[str]
    status: Optional[bool]
    R: Optional[str]
    G: Optional[str]
    B: Optional[str]

class LedDetails(BaseModel):
    id: int
    device_id: int
    name: str
    room: str
    type: str

class LedDetailsPut(BaseModel):
    device_id: Optional[int]
    name: Optional[str]
    room: Optional[str]
    type: Optional[str]

class Mechanics(BaseModel):
    id: int
    values: str

class MechanicsPut(BaseModel):
    values: Optional[str]

class MechanicsDetails(BaseModel):
    id: int
    device_id: int
    name: str
    room: str
    type: str

class MechanicsDetailsPut(BaseModel):
    device_id: Optional[int]
    name: Optional[str]
    room: Optional[str]
    type: Optional[str]

class Eb(BaseModel):
    id: int
    voltage: int
    amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int

class EbPut(BaseModel):
    voltage: Optional[int]
    amp: Optional[float]
    status: Optional[bool]
    ups_voltage: Optional[int]
    ups_AMP: Optional[int]
    ups_battery_percentage: Optional[int]

class EbStatus(BaseModel):
    id: int
    status: bool
    time_stamp: int

class UpsVoltage(BaseModel):
    device_id: int
    voltage: int
    time_stamp: int

class UpsAmpere(BaseModel):
    device_id: int
    ampere: float
    time_stamp: int

class Eb3(BaseModel):
    id: int
    R_voltage: int
    Y_voltage: int
    B_voltage: int
    R_amp: float
    Y_amp: float
    B_amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int

class Eb3Put(BaseModel):
    R_voltage: Optional[int]
    Y_voltage: Optional[int]
    B_voltage: Optional[int]
    R_amp: Optional[float]
    Y_amp: Optional[float]
    B_amp: Optional[float]
    status: Optional[bool]
    ups_voltage: Optional[int]
    ups_AMP: Optional[int]
    ups_battery_percentage: Optional[int]

class Eb3Voltage(BaseModel):
    device_id: int
    r_voltage: int
    y_voltage: int
    b_voltage: int
    time_stamp: int

class Eb3VoltagePut(BaseModel):
    r_voltage: Optional[int]
    y_voltage: Optional[int]
    b_voltage: Optional[int]
    time_stamp: Optional[int]

class Eb3Ampere(BaseModel):
    device_id: int
    r_ampere: float
    y_ampere: float
    b_ampere: float
    time_stamp: int

class Eb3AmperePut(BaseModel):
    device_id: Optional[int]
    r_ampere: Optional[float]
    y_ampere: Optional[float]
    b_ampere: Optional[float]
    time_stamp: Optional[int]

class Rooms(BaseModel):
    id: int
    name: str
    devices: list[int]
    fan: list[int]
    led: list[int]
    mechanics: list[int]
    motion_sensor: list[int]
    wta: list[int]

class RoomsPut(BaseModel):
    name: Optional[str]
    devices: Optional[list[int]]
    fan: Optional[list[int]]
    led: Optional[list[int]]
    mechanics: Optional[list[int]]
    motion_sensor: Optional[list[int]]

class Temperature(BaseModel):
    device_id: int
    room: str
    temperature: float
    humidity: float
    timestamp: int

class Log(BaseModel):
    device_id: int
    status: str
    timestamp: int
    updated_by: str

class MotionSensor(BaseModel):
    id: int
    ss: bool
    on_s: bool
    off_s: bool
    time: int

class MotionSensorPut(BaseModel):
    ss: Optional[bool]
    on_s: Optional[bool]
    off_s: Optional[bool]
    time: Optional[int]

class MotionSensorDetails(BaseModel):
    id: int
    device_id: int
    name: str
    room: str
    type: str

class MotionSensorDetailsPut(BaseModel):
    device_id: Optional[int]
    name: Optional[str]
    room: Optional[str]
    type: Optional[str]

class Wta(BaseModel):
    id: int
    level: int
    preset_value:int

class WtaPut(BaseModel):
    level: Optional[int]
    preset_value: Optional[int]

class wtaDetails(BaseModel):
    id: int
    device_id: int
    name: str
    room: str
    type: str

class wtaDetailsPut(BaseModel):
    device_id: Optional[int]
    name: Optional[str]
    room: Optional[str]
    type: Optional[str]