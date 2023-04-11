from pydantic import BaseModel


class Devices(BaseModel):
    id: int
    status: bool

class DevicesPut(BaseModel):
    status: bool

class DeviceDetails(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class DevicesDetailsPut(BaseModel):
    device_id: int
    name: str
    room: str
    type: str

class Fan(BaseModel):
    id: int
    status: bool
    speed: int

class FanPut(BaseModel):
    status: bool
    speed: int

class FanDetails(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class Led(BaseModel):
    id: int
    brightness: str
    status: bool
    R: str
    G: str
    B: str

class LedPut(BaseModel):
    brightness: str
    status: bool
    R: str
    G: str
    B: str

class LedDetails(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class Mechanics(BaseModel):
    id: int
    values: str

class MechanicsPut(BaseModel):
    id: int
    values: str

class MechanicsDetails(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class Eb(BaseModel):
    id: int
    voltage: int
    amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int

class EbPut(BaseModel):
    voltage: int
    amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int

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

class Eb3Voltage(BaseModel):
    device_id: int
    r_voltage: int
    y_voltage: int
    b_voltage: int
    time_stamp: int

class Eb3VoltagePut(BaseModel):
    r_voltage: int
    y_voltage: int
    b_voltage: int
    time_stamp: int

class Eb3Ampere(BaseModel):
    device_id: int
    r_ampere: float
    y_ampere: float
    b_ampere: float
    time_stamp: int

class Eb3AmperePut(BaseModel):
    device_id: int
    r_ampere: float
    y_ampere: float
    b_ampere: float
    time_stamp: int

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
    name: str
    devices: list[int]
    fan: list[int]
    led: list[int]
    mechanics: list[int]
    motion_sensor: list[int]

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

class Wta(BaseModel):
    id: int
    level: int

class MotionSensor(BaseModel):
    id: int
    ss: bool
    on_s: bool
    off_s: bool
    time: int

class MotionSensorPut(BaseModel):
    ss: bool
    on_s: bool
    off_s: bool
    time: int

class MotionSensorDetails(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class MotionSensorDetailsPut(BaseModel):
    device_id: int
    device_name: str
    room: str
    type: str