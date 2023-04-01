from pydantic import BaseModel


class Devices(BaseModel):
    id: int
    status: bool

class DeviceDetails(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class Devices_details_Put(BaseModel):
    device_id: int
    name: str
    room: str
    type: str

class Fan_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class Mechanics_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class Led_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class Log(BaseModel):
    device_id: int
    status: str
    timestamp: int
    updated_by: str

class Devices_put(BaseModel):
    status: bool

class Led(BaseModel):
    id: int
    brightness: str
    status: bool
    R: str
    G: str
    B: str

class Led_put(BaseModel):
    brightness: str
    status: bool
    R: str
    G: str
    B: str

class Fan(BaseModel):
    id: int
    status: bool
    speed: int

class Fan_put(BaseModel):
    status: bool
    speed: int

class Temperature(BaseModel):
    device_id: int
    room: str
    temperature: float
    humidity: float
    timestamp: int

class Mechanics(BaseModel):
    id: int
    values: str

class Mechanics_put(BaseModel):
    id: int
    values: str

class Wta(BaseModel):
    id: int
    level: int

class Eb(BaseModel):
    id: int
    voltage: int
    amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int

class Eb_put(BaseModel):
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

class Eb3_put(BaseModel):
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

class Eb3Ampere(BaseModel):
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

class MotionSensor(BaseModel):
    id: int
    ss: bool
    on_s: bool
    off_s: bool
    time: int

class MotionSensor_Put(BaseModel):
    ss: bool
    on_s: bool
    off_s: bool
    time: int

class MotionSensor_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str

class MotionSensor_details_put(BaseModel):
    device_id: int
    device_name: str
    room: str
    type: str