import time
from fastapi import FastAPI, Request
from models import *
from mongo import *
import uvicorn

app = FastAPI(title="Onwords Local Smart Home Server", docs_url="/admin", redoc_url="/document")

@app.get("/device/all", tags=["Devices"], description="Get All Devices", summary="Get All Devices")
async def getAllDevices():
    device_list = []
    documents = device_collections.find()
    for document in documents:
        device_list.append(document)
    return device_list

@app.get("/device/{item_id}", tags=["Devices"], description="Get Device By ID", summary="Get Device By ID")
async def getDeviceById(item_id: int):
    existing_device = device_collections.find_one({"_id": item_id})
    if existing_device is None:
        return {"message": f"device with ID {item_id} not found."}
    else:
        return device_collections.find_one({"_id": item_id})

@app.post("/device/create", tags=["Devices"], description="Create New Device", summary="Create New Device" )
async def createDevice(devices: Devices, request: Request):
    try:
        device_collections.insert_one({
            "_id": devices.id,
            "status": devices.status
        })
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = device_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}

@app.put("/device/update/{item_id}", tags=["Devices"], description="Update Device By ID", summary="Update Device By ID")
def updateDeviceById(device: DevicesPut, item_id: int):
    existing_device = device_collections.find_one({"_id": item_id})
    if existing_device is None:
        return {"message": f"device with ID {item_id} not found."}
    update_fields = {}
    if  device.status is not None:
        update_fields['status'] = device.status
    device_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/device/delete/{item_id}", tags=["Devices"], description="Delete Device By ID", summary="Delete Device By ID")
async def deleteDeviceById(item_id: int):
    existing_device = device_collections.find_one({"_id": item_id})
    if existing_device is None:
        return {"message": f"device with ID {item_id} not found."}
    else:
        device_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/device/details/all", tags=["Devices"], description="Get All Device Details", summary="Get All Device Details")
async def getAllDeviceDetails():
    device_list = []
    documents = device_detail_collections.find()
    for document in documents:
        device_list.append(document)
    return device_list

@app.get("/device/details/{item_id}", tags=["Devices"], description="Get Device Details By ID", summary="Get Device Details By ID")
async def getDeviceDetailsById(item_id: int):
    existing_device = device_detail_collections.find_one({"_id": item_id})
    if existing_device is None:
        return {"message": f"device with ID {item_id} not found."}
    else:
        return device_detail_collections.find_one({"_id": item_id})

@app.post("/device/details/create", tags=["Devices"], description="Create New Device Details", summary="Create New Device Details")
async def createDeviceDetails(devices: DeviceDetails, request: Request):
    try:
        device_detail_collections.insert_one({
            "_id": devices.id,
            "name": devices.name,
            "room": devices.room,
            "device_id": devices.device_id,
            "type": devices.type
        })
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = device_detail_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}

@app.put("/device/details/update/{item_id}", tags=["Devices"], description="Update Device Details By ID", summary="Update Device Details By ID")
def updateDeviceDetailsById(device: DevicesDetailsPut, item_id: int):
    existing_devices = device_detail_collections.find_one({"_id": item_id})
    if existing_devices is None:
        return {"message": f"Device with ID {item_id} not found."}
    update_fields = {}
    if device.name is not None:
        update_fields['name'] = device.name
    if device.room is not None:
        update_fields['room'] = device.room
    if  device.device_id is not None:
        update_fields['device_id'] = device.device_id
    if  device.type is not None:
        update_fields['type'] = device.type 
    device_detail_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/device/details/delete/{item_id}", tags=["Devices"], description="Delete Device Details By ID", summary="Delete Device Details By ID")
async def deleteDeviceDetailsById(item_id: int):
    existing_device = device_detail_collections.find_one({"_id": item_id})
    if existing_device is None:
        return {"message": f"device with ID {item_id} not found."}
    else:
        device_detail_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/device/log/all", tags=["Devices"], description="Get All Device Logs", summary="Get All Device Logs")
async def getAllDeviceLog():
    device_list = []
    documents = device_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/device/log/create", tags=["Devices"], description="Create New Device Log", summary="Create New Device Log")
async def createDeviceLog(devices: Log, request: Request):
    try:
        device_details_log_collections.insert_one({
            "_id": time.time(),
            "device_id": devices.device_id,
            "status": devices.status,
            "timestamp": devices.timestamp,
            "updated_by": devices.updated_by
        })
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        documents = device_details_log_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == devices.device_id:
                return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}
    
@app.get("/device/boardlog/all", tags=["Devices"], description="Get All Device Board Logs", summary="Get All Device Board Logs")
async def getAllBoardLog():
    device_list = []
    documents = device_board_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/device/boardlog/create", tags=["Devices"], description="Create New Device Board Log", summary="Create New Device Board Log")
async def createDeviceBoardLog(devices: Log, request: Request):
    try:
        device_board_log_collections.insert_one({
            "_id": time.time(),
            "device_id": devices.device_id,
            "status": devices.status,
            "timestamp": devices.timestamp,
            "updated_by": devices.updated_by
        })
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        documents = device_board_log_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == devices.device_id:
                return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}

@app.get("/fan/all", tags=["Fan"], description="Get All Fan", summary="Get All Fan")
async def getAllFans():
    fan_list = []
    documents = fan_collections.find()
    for document in documents:
        fan_list.append(document)
    return fan_list

@app.get("/fan/{item_id}", tags=["Fan"], description="Get Fan By ID", summary="Get Fan By ID")
async def getFanById(item_id: int):
    existing_fan = fan_collections.find_one({"_id": item_id})
    if existing_fan is None:
        return {"message": f"fan with ID {item_id} not found."}
    else:
        return fan_collections.find_one({"_id": item_id})

@app.post("/fan/create", tags=["Fan"], description="Create New Fan", summary="Create New Fan")
async def createFan(fan: Fan, request: Request):
    try:
        fan_collections.insert_one({"_id": fan.id, "status": fan.status, "speed": fan.speed})
        return {"msg": "created successfully", "created_data": fan, "client": request.client}
    except:
        documents = fan_collections.find()
        for document in documents:
            id = document["_id"]
            if id == fan.id:
                return {"msg": {f"id {fan.id} already exist in fan, try using other id"}}

@app.put("/fan/update/{item_id}", tags=["Fan"], description="Update Fan By ID", summary="Update Fan By ID")
def updateFanById(device: FanPut, item_id: int):
    existing_fan = fan_collections.find_one({"_id": item_id})
    if existing_fan is None:
        return {"message": f"fan with ID {item_id} not found."}
    update_fields = {}
    if  device.status is not None:
        update_fields['status'] =device.status
    if  device.speed is not None:
        update_fields['speed'] =device.speed
    fan_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/fan/delete/{item_id}", tags=["Fan"], description="Delete Fan By ID", summary="Delete Fan By ID")
async def deleteFanById(item_id: int):
    existing_fan = fan_collections.find_one({"_id": item_id})
    if existing_fan is None:
        return {"message": f"fan with ID {item_id} not found."}
    else:
        fan_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/fan/details/all", tags=["Fan"], description="Get All Fan Details", summary="Get All Fan Details")
async def getFanDetails():
    device_list = []
    documents = fan_details_collections.find()
    for document in documents:
        device_list.append(document)
    return device_list

@app.get("/fan/details/{item_id}", tags=["Fan"], description="Get Fan Details By ID", summary="Get Fan Details By ID")
async def getFanDetailsById(item_id: int):
    existing_fan = fan_details_collections.find_one({"_id": item_id})
    if existing_fan is None:
        return {"message": f"fan with ID {item_id} not found."}
    else:
        return fan_details_collections.find_one({"_id": item_id})

@app.post("/fan/details/create", tags=["Fan"], description="Create New Fan Details", summary="Create New Fan Details")
async def createFanDetails(devices: FanDetails, request: Request):
    try:
        fan_details_collections.insert_one({
            "_id": devices.id,
            "name": devices.name,
            "room": devices.room,
            "device_id": devices.device_id,
            "type": devices.type
        })
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = fan_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}

@app.put("/fan/details/update/{item_id}", tags=["Fan"], description="Update Fan Details By ID", summary="Update Fan Details By ID")
def updateFanDetailsById(device: FanDetailsPut, item_id: int):
    existing_fan = fan_details_collections.find_one({"_id": item_id})
    if existing_fan is None:
        return {"message": f"Fan with ID {item_id} not found."}
    update_fields = {}
    if device.name is not None:
        update_fields['name'] = device.name
    if device.room is not None:
        update_fields['room'] = device.room
    if  device.device_id is not None:
        update_fields['device_id'] = device.device_id
    if  device.type is not None:
        update_fields['type'] = device.type 
    fan_details_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/fan/details/delete/{item_id}", tags=["Fan"], description="Delete Fan Details By ID", summary="Delete Fan Details By ID")
async def deleteFanDetailsById(item_id: int):
    existing_fan = fan_details_collections.find_one({"_id": item_id})
    if existing_fan is None:
        return {"message": f"fan with ID {item_id} not found."}
    else:
        fan_details_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/fan/log/all", tags=["Fan"], description="Get All Fan Log", summary="Get All Fan Log")
async def getFanLog():
    device_list = []
    documents = fan_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/fan/log/create", tags=["Fan"], description="Create New Fan Log", summary="Create New Fan Log")
async def createFanLog(devices: Log, request: Request):
    try:
        fan_details_log_collections.insert_one({
            "_id": time.time(),
            "device_id": devices.device_id,
            "status": devices.status,
            "timestamp": devices.timestamp,
            "updated_by": devices.updated_by
        })
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        documents = fan_details_log_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == devices.device_id:
                return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}

@app.get("/fan/boardlog/all", tags=["Fan"], description="Get All Fan Board Log", summary="Get All Fan Board Log")
async def getFanBoardLog():
    device_list = []
    documents = fan_board_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/fan/boardlog/create", tags=["Fan"], description="Create New Fan Board Log", summary="Create New Fan Board Log")
async def createFanBoardLog(devices: Log, request: Request):
    try:
        fan_board_log_collections.insert_one({
            "_id": time.time(),
            "device_id": devices.device_id,
            "status": devices.status,
            "timestamp": devices.timestamp,
            "updated_by": devices.updated_by
        })
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        documents = fan_board_log_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == devices.device_id:
                return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}

@app.get("/led/all", tags=["LED"], description="Get All Led", summary="Get All Led")
async def getLed():
    list = []
    documents = led_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/led/{item_id}", tags=["LED"], description="Get Led By ID", summary="Get Led By ID")
async def getLedById(item_id: int):
    existing_led = led_collections.find_one({"_id": item_id})
    if existing_led is None:
        return {"message": f"led with ID {item_id} not found."}
    else:
        return led_collections.find_one({"_id": item_id})

@app.post("/led/create", tags=["LED"], description="Create New Led", summary="Create New Led")
async def createLed(led: Led, request: Request):
    try:
        led_collections.insert_one({"_id": led.id, "brightness": led.brightness, "status": led.status, "R": led.R, "G": led.G, "B": led.B})
        return {"msg": "created successfully", "created_data": led, "client": request.client}
    except:
        documents = led_collections.find()
        for document in documents:
            id = document["_id"]
            if id == led.id:
                return {"msg": {f"id {led.id} already exist in fan, try using other id"}}

@app.put("/led/update/{item_id}", tags=["LED"], description="Update Led By ID", summary="Update Led By ID")
def updateLedById(led: LedPut, item_id: int):
    existing_led = led_collections.find_one({"_id": item_id})
    if existing_led is None:
        return {"message": f"led with ID {item_id} not found."}
    update_fields = {}
    if  led.brightness is not None:
        update_fields['brightness'] =led.brightness
    if  led.status is not None:
        update_fields['status'] =led.status
    if  led.R is not None:
        update_fields['R'] =led.R
    if  led.G is not None:
        update_fields['G'] =led.G
    if  led.B is not None:
        update_fields['B'] =led.B
    led_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.delete("/led/delete/{item_id}", tags=["LED"], description="Delete Led By ID", summary="Delete Led By ID")
async def deleteLedById(item_id: int):
    existing_led = led_collections.find_one({"_id": item_id})
    if existing_led is None:
        return {"message": f"led with ID {item_id} not found."}
    else:
        led_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/led/details/all", tags=["LED"], description="Get All Led details", summary="Get All Led details")
async def getLedDetails():
    try:
        device_list = []
        documents = led_details_collections.find()
        for document in documents:
            device_list.append(document)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"

@app.get("/led/details/{item_id}", tags=["LED"], description="Get Led Details By ID", summary="Get Led Details By ID")
async def getLedDetailsById(item_id: int):
    existing_led = led_details_collections.find_one({"_id": item_id})
    if existing_led is None:
        return {"message": f"led with ID {item_id} not found."}
    else:
        return led_details_collections.find_one({"_id": item_id})

@app.post("/led/details/create", tags=["LED"], description="Create New Led Details", summary="Create New Led Details")
async def getLedDetails(devices: LedDetails, request: Request):
    try:
        led_details_collections.insert_one({
            "_id": devices.id,
            "name": devices.name,
            "room": devices.room,
            "device_id": devices.device_id,
            "type": devices.type
        })
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = led_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}

@app.put("/led/details/update/{item_id}", tags=["LED"], description="Update Led Details By ID", summary="Update Led Details By ID")
def updateLedDetailsById(device: LedDetailsPut, item_id: int):
    existing_led = led_details_collections.find_one({"_id": item_id})
    if existing_led is None:
        return {"message": f"Fan with ID {item_id} not found."}
    update_fields = {}
    if device.name is not None:
        update_fields['name'] = device.name
    if device.room is not None:
        update_fields['room'] = device.room
    if  device.device_id is not None:
        update_fields['device_id'] = device.device_id
    if  device.type is not None:
        update_fields['type'] = device.type 
    led_details_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/led/details/delete/{item_id}", tags=["LED"], description="Delete Led Details By ID", summary="Delete Led Details By ID")
async def deleteLedDetailsById(item_id: int):
    existing_led = led_details_collections.find_one({"_id": item_id})
    if existing_led is None:
        return {"message": f"led with ID {item_id} not found."}
    else:
        led_details_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/led/log/all", tags=["LED"], description="Get All Led Log", summary="Get All Led Log")
async def getLedLog():
    device_list = []
    documents = led_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/led/log/create", tags=["LED"], description="Create New Led Log", summary="Create New Led Log")
async def getLedLog(devices: Log, request: Request):
    try:
        led_details_log_collections.insert_one({
            "_id": time.time(),
            "device_id": devices.device_id,
            "status": devices.status,
            "timestamp": devices.timestamp,
            "updated_by": devices.updated_by
        })
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}

@app.get("/mechanics/all", tags=["Mechanics"], description="Get All Mechanics", summary="Get All Mechanics")
async def getMechanics():
    list = []
    documents = mechanics_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/mechanics/{item_id}", tags=["Mechanics"], description="Get Mechanics By ID", summary="Get Mechanics By ID")
async def getMechanicsById(item_id: int):
    existing_mechanics = mechanics_collections.find_one({"_id": item_id})
    if existing_mechanics is None:
        return {"message": f"Mechanics with ID {item_id} not found."}
    else:
        return mechanics_collections.find_one({"_id": item_id})

@app.post("/mechanics/create", tags=["Mechanics"], description="Create New Mechanics", summary="Create New Mechanics")
async def createMechanics(mechanics: Mechanics, request: Request):
    try:
        mechanics_collections.insert_one({"_id": mechanics.id, "values": mechanics.values})
        return {"msg": "created successfully", "created_data": mechanics, "client": request.client}
    except:
        documents = mechanics_collections.find()
        for document in documents:
            id = document["_id"]
            if id == mechanics.id:
                return {"msg": {f"id {mechanics.id} already exist in fan, try using other id"}}

@app.put("/mechanics/update/{item_id}", tags=["Mechanics"], description="Update Mechanics By ID", summary="Update Mechanics By ID")
def updateMechanicsById(mechanics: MechanicsPut, item_id: int):
    existing_mechanics = mechanics_collections.find_one({"_id": item_id})
    if existing_mechanics is None:
        return {"message": f"Mechanics with ID {item_id} not found."}
    update_fields = {}
    if  mechanics.values is not None:
        update_fields['values'] =mechanics.values
    mechanics_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.delete("/mechanics/delete/{item_id}", tags=["Mechanics"], description="Delete Mechanics By ID", summary="Delete Mechanics By ID")
async def deleteMechanicsById(item_id: int):
    existing_mechanics = mechanics_collections.find_one({"_id": item_id})
    if existing_mechanics is None:
        return {"message": f"Mechanics with ID {item_id} not found."}
    else:
        mechanics_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/mechanics/details/all", tags=["Mechanics"], description="Get All Mechanics Details", summary="Get All Mechanics Details")
async def getMechanicsDetails():
    device_list = []
    documents = mechanics_details_collections.find()
    for document in documents:
        device_list.append(document)
    return device_list

@app.get("/mechanics/details/{item_id}", tags=["Mechanics"], description="Get Mechanics Details By ID", summary="Get Mechanics Details By ID")
async def getMechanicsDetailsById(item_id: int):
    existing_mechanicsdetailes = mechanics_details_collections.find_one({"_id": item_id})
    if existing_mechanicsdetailes is None:
        return {"message": f"Mechanics with ID {item_id} not found."}
    else:
        return mechanics_details_collections.find_one({"_id": item_id})

@app.post("/mechanics/details/create", tags=["Mechanics"], description="Create New Mechanics details", summary="Create New Mechanics details")
async def createMechanicsDetails(devices: MechanicsDetails, request: Request):
    try:
        mechanics_details_collections.insert_one({
            "_id": devices.id,
            "name": devices.name,
            "room": devices.room,
            "device_id": devices.device_id,
            "type": devices.type
        })
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = mechanics_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}

@app.put("/mechanics/details/update/{item_id}", tags=["Mechanics"], description="Update Mechanics Details By ID", summary="Update Mechanics Details By ID")
def updateMechanicsDetailsById(device: MechanicsDetailsPut, item_id: int):
    existing_led = mechanics_details_collections.find_one({"_id": item_id})
    if existing_led is None:
        return {"message": f"Fan with ID {item_id} not found."}
    update_fields = {}
    if device.name is not None:
        update_fields['name'] = device.name
    if device.room is not None:
        update_fields['room'] = device.room
    if  device.device_id is not None:
        update_fields['device_id'] = device.device_id
    if  device.type is not None:
        update_fields['type'] = device.type 
    mechanics_details_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/mechanics/details/delete/{item_id}", tags=["Mechanics"], description="Delete Mechanics Details By ID", summary="Delete Mechanics Details By ID")
async def deleteMechanicsDetailsById(item_id: int):
    existing_mechanicsdetailes = mechanics_details_collections.find_one({"_id": item_id})
    if existing_mechanicsdetailes is None:
        return {"message": f"Mechanics with ID {item_id} not found."}
    else:
        mechanics_details_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/mechanics/log/all", tags=["Mechanics"], description="Get All mechanics Log", summary="Get All mechanics Log")
async def getMechanicsLog():
    device_list = []
    documents = mechanics_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/mechanics/log/create", tags=["Mechanics"], description="Create New Mechanics Log", summary="Create New Mechanics Log")
async def createMechanicsLog(devices: Log, request: Request):
    try:
        mechanics_details_log_collections.insert_one({
            "_id": time.time(),
            "device_id": devices.device_id,
            "status": devices.status,
            "timestamp": devices.timestamp,
            "updated_by": devices.updated_by
        })
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id already exist in devices log, try using other id"}}

@app.get("/eb/all", tags=["EB"], description="Get All Eb", summary="Get All Eb") 
async def getEb():
    list = []
    documents = eb_sensor_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/eb/{item_id}", tags=["EB"], description="Get Eb By ID", summary="Get Eb By ID")
async def getEbById(item_id: int):
    existing_eb = eb_sensor_collections.find_one({"_id": item_id})
    if existing_eb is None:
        return {"message": f"eb with ID {item_id} not found."}
    else:
        return eb_sensor_collections.find_one({"_id": item_id})

@app.post("/eb/create", tags=["EB"], description="Create New Eb", summary="Create New Eb")
async def createEb(eb: Eb, request: Request):
    try:
        eb_sensor_collections.insert_one({
            "_id": eb.id,
            "voltage": eb.voltage,
            "amp": eb.amp,
            "ups_voltage": eb.ups_voltage,
            "ups_amp": eb.ups_AMP,
            "status": eb.status,
            "ups_battery_percentages": eb.ups_battery_percentage
        })
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_sensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}

@app.put("/eb/update/{item_id}", tags=["EB"], description="Update Eb By ID", summary="Update Eb By ID")
def updateEbById(eb: EbPut, item_id: int):
    existing_eb = eb_sensor_collections.find_one({"_id": item_id})
    if existing_eb is None:
        return {"message": f"eb with ID {item_id} not found."}
    update_fields = {}
    if eb.voltage is not None:
        update_fields['voltage'] = eb.voltage
    if  eb.amp is not None:
        update_fields['amp'] = eb.amp
    if  eb.ups_voltage is not None:
        update_fields['ups_voltage'] = eb.ups_voltage
    if  eb.ups_AMP is not None:
        update_fields['ups_AMP'] =eb.ups_AMP
    if  eb.status is not None:
        update_fields['status'] =eb.status
    if  eb.ups_battery_percentage is not None:
        update_fields['ups_battery_percentage'] =eb.ups_battery_percentage
    eb_sensor_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.delete("/eb/delete/{item_id}", tags=["EB"], description="Delete Eb By ID", summary="Delete Eb By ID")
async def deleteEbById(item_id: int):
    existing_eb = eb_sensor_collections.find_one({"_id": item_id})
    if existing_eb is None:
        return {"message": f"eb with ID {item_id} not found."}
    else:
        eb_sensor_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/eb/status/all", tags=["EB"], description="Get All Eb Status", summary="Get All Eb Status")
async def getEbStatus():
    list = []
    documents = eb_status_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/eb/status/{item_id}", tags=["EB"], description="Get Eb Status By ID", summary="Get Eb Status By ID")
async def getEbStatusById(item_id: int):
    existing_eb_status = eb_status_collections.find_one({"_id": item_id})
    if existing_eb_status is None:
        return {"message": f"eb with ID {item_id} not found."}
    else:
        return eb_status_collections.find_one({"_id": item_id})

@app.post("/eb/status/create", tags=["EB"], description="Create New Eb Status", summary="Create New Eb Status")
async def createEbStatus(eb: EbStatus, request: Request):
    try:
        eb_status_collections.insert_one({
            "_id": eb.id,
            "status": eb.status,
            "time_stamp": eb.time_stamp
        })
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_status_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}

@app.get("/ups/voltage/all", tags=["EB"], description="Get All Ups Voltage", summary="Get All Ups Voltage")
async def getUpsVoltage():
    list = []
    documents = eb_ups_voltage_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/ups/voltage/{item_id}", tags=["EB"], description="Get Ups Voltage By ID", summary="Get Ups Voltage By ID")
async def getUpsVoltageById(item_id: int):
    existing_ups_voltage = eb_ups_voltage_collections.find_one({"device_id": item_id})
    if existing_ups_voltage is None:
        return {"message": f"ups with ID {item_id} not found."}
    else:
        return eb_ups_voltage_collections.find_one({"device_id": item_id})

@app.post("/ups/voltage/create", tags=["EB"], description="Create New Ups Voltage", summary="Create New Ups Voltage")
async def createUpsVoltage(eb: UpsVoltage, request: Request):
    try:
        eb_ups_voltage_collections.insert_one({
            "_id": time.time(),
            "device_id": eb.device_id,
            "voltage": eb.voltage,
            "time_stamp": eb.time_stamp
        })
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_ups_voltage_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}

@app.get("/ups/ampere/all", tags=["EB"], description="Get All Ups Ampere", summary="Get All Ups Ampere")
async def getUpsAmpere():
    list = []
    documents = eb_ups_ampere_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/ups/ampere/{item_id}", tags=["EB"], description="Get Ups Ampere By ID", summary="Get Ups Ampere By ID")
async def getUpsAmpereById(item_id: int):
    existing_ups = eb_ups_ampere_collections.find_one({"device_id": item_id})
    if existing_ups is None:
        return {"message": f"ups with ID {item_id} not found."}
    else:
        return eb_ups_ampere_collections.find_one({"device_id": item_id})

@app.post("/ups/ampere/create", tags=["EB"], description="Create New Ups Ampere", summary="Create New Ups Ampere")
async def createUpsAmpere(eb: UpsAmpere, request: Request):
    try:
        eb_ups_ampere_collections.insert_one({
            "_id": time.time(),
            "device_id": eb.device_id,
            "ampere": eb.ampere,
            "time_stamp": eb.time_stamp
        })
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_ups_ampere_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}

@app.get("/eb3/all", tags=["EB 3 Phase"], description="Get All Eb3", summary="Get All Eb3")
async def getEb3():
    list = []
    documents = eb3phasae_sensor_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/eb3/{item_id}", tags=["EB 3 Phase"], description="Get Eb3 By ID", summary="Get Eb3 By ID")
async def getEb3ById(item_id: int):
    existing_eb3 = eb3phasae_sensor_collections.find_one({"_id": item_id})
    if existing_eb3 is None:
        return {"message": f"eb3 with ID {item_id} not found."}
    else:
        return eb3phasae_sensor_collections.find_one({"_id": item_id})

@app.post("/eb3/create", tags=["EB 3 Phase"], description="Create New Eb3", summary="Create New Eb3")
async def createEb3(eb3: Eb3, request: Request):
    try:
        eb3phasae_sensor_collections.insert_one({
            "_id": eb3.id,
            "R_voltage": eb3.R_voltage,
            "Y_voltage": eb3.Y_voltage,
            "B_voltage": eb3.B_voltage,
            "R_amp": eb3.R_amp,
            "Y_amp": eb3.Y_amp,
            "B_amp": eb3.B_amp,
            "ups_voltage": eb3.ups_voltage,
            "ups_AMP": eb3.ups_AMP,
            "ups_battery_percentage": eb3.ups_battery_percentage,
            "status": eb3.status
        })
        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_sensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb3.id:
                return {"msg": {f"id {eb3.id} already exist in fan, try using other id"}}

@app.put("/eb3/update/{item_id}", tags=["EB 3 Phase"], description="Update Eb3 By ID ", summary="Update Eb3 By ID ")
def updateEb3ById(eb3: Eb3Put, item_id: int):
    existing_eb3 = eb3phasae_sensor_collections.find_one({"_id": item_id})
    if existing_eb3 is None:
        return {"message": f"eb3 with ID {item_id} not found."}
    update_fields = {}
    if eb3.R_voltage is not None:
        update_fields['R_voltage'] = eb3.R_voltage
    if  eb3.Y_voltage is not None:
        update_fields['Y_voltage'] = eb3.Y_voltage
    if  eb3.B_voltage is not None:
        update_fields['B_voltage'] = eb3.B_voltage
    if  eb3.R_amp is not None:
        update_fields['R_amp'] =eb3.R_amp
    if  eb3.Y_amp is not None:
        update_fields['Y_amp'] =eb3.Y_amp
    if  eb3.B_amp is not None:
        update_fields['B_amp'] =eb3.B_amp
    if  eb3.ups_voltage is not None:
        update_fields['ups_voltage'] =eb3.ups_voltage
    if  eb3.ups_AMP is not None:
        update_fields['ups_AMP'] =eb3.ups_AMP
    if  eb3.ups_battery_percentage is not None:
        update_fields['ups_battery_percentage'] =eb3.ups_battery_percentage
    if  eb3.status is not None:
        update_fields['status'] =eb3.status
    eb3phasae_sensor_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.delete("/eb3/delete/{item_id}", tags=["EB 3 Phase"], description="Delete Eb3 By ID", summary="Delete Eb3 By ID")
async def deleteEb3ById(item_id: int):
    existing_eb3 = eb3phasae_sensor_collections.find_one({"_id": item_id})
    if existing_eb3 is None:
        return {"message": f"eb3 with ID {item_id} not found."}
    else:
        eb3phasae_sensor_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/eb3/voltage/all", tags=["EB 3 Phase"], description="Get All Eb3 Voltage", summary="Get All Eb3 Voltage")
async def getEb3Voltage():
    list = []
    documents = eb3phasae_voltage_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/eb3/voltage/{item_id}", tags=["EB 3 Phase"], description="Get Eb3 Voltage By ID", summary="Get Eb3 Voltage By ID")
async def getEb3VoltageById(item_id: int):
    existing_eb3voltage = eb3phasae_voltage_collections.find_one({"device_id": item_id})
    if existing_eb3voltage is None:
        return {"message": f"eb3 with ID {item_id} not found."}
    else:
        return eb3phasae_voltage_collections.find_one({"device_id": item_id})

@app.post("/eb3/voltage/create", tags=["EB 3 Phase"], description="Create New Eb3 Voltage", summary="Create New Eb3 Voltage")
async def createEb3Voltage(eb3: Eb3Voltage, request: Request):
    try:
        eb3phasae_voltage_collections.insert_one({
            "_id": time.time(),
            "device_id": eb3.device_id,
            "r_voltage": eb3.r_voltage,
            "y_voltage": eb3.y_voltage,
            "b_voltage": eb3.b_voltage,
            "time_stamp": eb3.time_stamp
        })
        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_voltage_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == eb3.device_id:
                return {"msg": {f"id {eb3.device_id} already exist in fan, try using other id"}}

@app.put("/eb3/voltage/update/{item_id}", tags=["EB 3 Phase"], description="Update Eb3 Voltage By ID", summary="Update Eb3 Voltage By ID")
def updateEb3VoltageById(eb3: Eb3VoltagePut, item_id: int):
    existing_eb3voltage = eb3phasae_voltage_collections.find_one({"device_id": item_id})
    if existing_eb3voltage is None:
        return {"message": f"eb3 with ID {item_id} not found."}
    update_fields = {}
    if eb3.r_voltage is not None:
        update_fields['r_voltage'] = eb3.r_voltage
    if  eb3.y_voltage is not None:
        update_fields['y_voltage'] = eb3.y_voltage
    if  eb3.b_voltage is not None:
        update_fields['b_voltage'] = eb3.b_voltage
    if  eb3.time_stamp is not None:
        update_fields['time_stamp'] =eb3.time_stamp
    eb3phasae_voltage_collections.update_one(
        {"device_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.get("/eb3/ampere/all", tags=["EB 3 Phase"], description="Get All Eb3 Ampere", summary="Get All Eb3 Ampere")
async def getEb3Ampere():
    list = []
    documents = eb3phasae_ampere_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/eb3/ampere/{item_id}", tags=["EB 3 Phase"], description="Get Eb3 Ampere By ID", summary="Get Eb3 Ampere By ID")
async def getEb3AmpereById(item_id: int):
    existing_eb3amphere = eb3phasae_ampere_collections.find_one({"device_id": item_id})
    if existing_eb3amphere is None:
        return {"message": f"eb3 with ID {item_id} not found."}
    else:
        return eb3phasae_ampere_collections.find_one({"device_id": item_id})

@app.post("/eb3/ampere/create", tags=["EB 3 Phase"], description="Create New Eb3 Ampere", summary="Create New Eb3 Ampere")
async def createEb3Ampere(eb3: Eb3Ampere, request: Request):
    try:
        eb3phasae_ampere_collections.insert_one({
            "_id": time.time(),
            "device_id": eb3.device_id,
            "r_ampere": eb3.r_ampere,
            "y_ampere": eb3.y_ampere,
            "b_ampere": eb3.b_ampere,
            "time_stamp": eb3.time_stamp
        })

        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_ampere_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb3.id:
                return {"msg": {f"id {eb3.id} already exist in fan, try using other id"}}

@app.put("/eb3/ampere/update/{item_id}", tags=["EB 3 Phase"], description="Update Eb3 Ampere By ID", summary="Update Eb3 Ampere By ID")
def updateEb3AmpereById(eb3: Eb3AmperePut, item_id: int):
    existing_eb3amphere = eb3phasae_ampere_collections.find_one({"device_id": item_id})
    if existing_eb3amphere is None:
        return {"message": f"eb3 with ID {item_id} not found."}
    update_fields = {}
    if eb3.r_ampere is not None:
        update_fields['r_ampere'] = eb3.r_ampere
    if  eb3.y_ampere is not None:
        update_fields['y_ampere'] = eb3.y_ampere
    if  eb3.b_ampere is not None:
        update_fields['b_ampere'] = eb3.b_ampere
    if  eb3.time_stamp is not None:
        update_fields['time_stamp'] =eb3.time_stamp
    eb3phasae_ampere_collections.update_one(
        {"device_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.get("/room/all", tags=["Rooms"], description="Get All Room", summary="Get All Room")
async def getRoom():
    room_list = []
    documents = room_collections.find()
    for document in documents:
        room_list.append(document)
    return room_list

@app.get("/room/{item_id}", tags=["Rooms"], description="Get Room By ID", summary="Get Room By ID")
async def getRoomById(item_id: int):
    existing_room = room_collections.find_one({"_id": item_id})
    if existing_room is None:
        return {"message": f"room with ID {item_id} not found."}
    else:
        return room_collections.find_one({"_id": item_id})

@app.post("/room/create", tags=["Rooms"], description="Create New Room", summary="Create New Room")
async def createRoom(room: Rooms, request: Request):
    try:
        room_collections.insert_one({
            "_id": room.id,
            "name": room.name,
            "device_id": room.devices,
            "fan_id": room.fan,
            "led_id": room.led,
            "mechanics_id": room.mechanics,
            "motion_sensor_id": room.motion_sensor
        })
        return {"msg": "created successfully", "created_data": room, "client": request.client}
    except:
        documents = room_collections.find()
        for document in documents:
            id = document["_id"]
            if id == room.id:
                return {"msg": {f"id {room.id} already exist in rooms, try using other id"}}

@app.put("/room/update/{item_id}", tags=["Rooms"], description="Update Room By ID", summary="Update Room By ID")
async def updateRoomById(rooms: RoomsPut, item_id: int):
    existing_room = room_collections.find_one({"_id": item_id})
    if existing_room is None:
        return {"message": f"room with ID {item_id} not found."}
    update_fields = {}
    if rooms.name is not None:
        update_fields['name'] = rooms.name
    if rooms.devices is not None:
        update_fields['devices'] = rooms.devices
    if  rooms.fan is not None:
        update_fields['fan'] = rooms.fan
    if  rooms.mechanics is not None:
        update_fields['mechanics'] = rooms.mechanics
    if  rooms.motion_sensor is not None:
        update_fields['motion_sensor'] = rooms.motion_sensor
    room_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.delete("/room/delete/{item_id}", tags=["Rooms"], description="Delete Room By ID", summary="Delete Room By ID")
async def deleteRoomById(item_id: int):
    existing_room = room_collections.find_one({"_id": item_id})
    if existing_room is None:
        return {"message": f"room with ID {item_id} not found."}
    else:
        room_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/temp/all", tags=["Temperature"], description="Get All Temp", summary="Get All Temp")
async def getTemp():
    room_list = []
    documents = temp_collections.find()
    for document in documents:
        room_list.append(document)
    return room_list

@app.post("/temp/create", tags=["Temperature"], description="Create New Temp", summary="Create New Temp")
async def createTemp(temp: Temperature, request: Request):
    try:
        temp_collections.insert_one({
            "_id": time.time(),
            "device_id": temp.device_id,
            "room": temp.room,
            "temperature": temp.temperature,
            "humidity": temp.humidity,
            "timestamp": temp.timestamp
        })
        return {"msg": "created successfully", "created_data": temp, "client": request.client}
    except:
        documents = temp_collections.find()
        for document in documents:
            id = document["_id"]
            if id == temp.device_id:
                return {"msg": {f"id {temp.device_id} already exist in temp, try using other id"}}

@app.get("/motionsensor/all", tags=["Motion Sensor"], description="Get All Motionsensor", summary="Get All Motionsensor")
async def getMotionsensor():
    list = []
    documents = motionsensor_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/motionsensor/{item_id}", tags=["Motion Sensor"], description="Get Motionsensor By ID", summary="Get Motionsensor By ID")
async def getMotionsensorById(item_id: int):
    existing_motion = motionsensor_collections.find_one({"_id": item_id})
    if existing_motion is None:
        return {"message": f"Motion sensor with ID {item_id} not found."}
    else:
        return motionsensor_collections.find_one({"_id": item_id})

@app.post("/motionsensor/create", tags=["Motion Sensor"], description="Create New Motionsensor", summary="Create New Motionsensor")
async def createMotionsensor(ms: MotionSensor, request: Request):
    try:
        motionsensor_collections.insert_one(
            {
                "_id": ms.id,
                "ss": ms.ss,
                "on_s": ms.on_s,
                "off_s": ms.off_s,
                "time": ms.time
            }
        )
        return {"msg": "created successfully", "created_data": ms, "client": request.client}
    except:
        documents = motionsensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == ms.id:
                return {"msg": {f"id {ms.id} already exist in fan, try using other id"}}

@app.put("/motionsensor/update/{item_id}", tags=["Motion Sensor"], description="Update Motionsensor By ID", summary="Update Motionsensor By ID")
async def updateMotionsensor(motion: MotionSensorPut, item_id: int):
    existing_motion = motionsensor_collections.find_one({"_id": item_id})
    if existing_motion is None:
        return {"message": f"Motion sensor with ID {item_id} not found."}
    update_fields = {}
    if motion.ss is not None:
        update_fields['ss'] = motion.ss
    if motion.on_s is not None:
        update_fields['on_s'] = motion.on_s
    if  motion.off_s is not None:
        update_fields['off_s'] = motion.off_s
    if  motion.time is not None:
        update_fields['time'] = motion.time 
    motionsensor_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.delete("/motionsensor/delete/{item_id}", tags=["Motion Sensor"], description="Delete Motionsensor By ID", summary="Delete Motionsensor By ID")
async def deleteMotionsensor(item_id: int):
    existing_motion = motionsensor_collections.find_one({"_id": item_id})
    if existing_motion is None:
        return {"message": f"Motion sensor with ID {item_id} not found."}
    else:
        motionsensor_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/motionsensor/details/all", tags=["Motion Sensor"], description="Get All Motionsensor Details", summary="Get All Motionsensor Details")
async def getMotionsensorDetails():
    list = []
    documents = motionsensor_details_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/motionsensor/details/{item_id}", tags=["Motion Sensor"], description="Get MotionSensor Details By ID", summary="Get MotionSensor Details By ID")
async def getMotionsensorDetailsById(item_id: int):
    existing_motion = motionsensor_details_collections.find_one({"_id": item_id})
    if existing_motion is None:
        return {"message": f"Motion sensor with ID {item_id} not found."}
    else:
        return motionsensor_details_collections.find_one({"_id": item_id})

@app.post("/motionsensor/details/create", tags=["Motion Sensor"], description="Create New Motionsensor Details", summary="Create New Motionsensor Details")
async def createMotionsensorDetails(devices: MotionSensorDetails, request: Request):
    try:
        motionsensor_details_collections.insert_one({
            "_id": devices.id,
            "name": devices.name,
            "room": devices.room,
            "device_id": devices.device_id,
            "type": devices.type
        })
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = motionsensor_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}

@app.put("/motionsensor/details/update/{item_id}", tags=["Motion Sensor"], description="Update Motionsensor Details By ID", summary="Update Motionsensor Details By ID")
def updateMotionsensorDetailsById(device: MotionSensorDetailsPut, item_id: int):
    existing_motion = motionsensor_details_collections.find_one({"_id": item_id})
    if existing_motion is None:
        return {"message": f"Motion sensor with ID {item_id} not found."}
    update_fields = {}
    if device.name is not None:
        update_fields['name'] = device.name
    if device.room is not None:
        update_fields['room'] = device.room
    if  device.device_id is not None:
        update_fields['device_id'] = device.device_id
    if  device.type is not None:
        update_fields['type'] = device.type 
    motionsensor_details_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/motionsensor/details/delete/{item_id}", tags=["Motion Sensor"], description="Delete Motionsensor Details By ID", summary="Delete Motionsensor Details By ID")
async def deleteMotionsensorDetailsById(item_id: int):
    existing_motion = motionsensor_details_collections.find_one({"_id": item_id})
    if existing_motion is None:
        return {"message": f"Motion sensor with ID {item_id} not found."}
    else:
        motionsensor_details_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/wta/all", tags=["WTA"], description="Get All WTA", summary="Get All WTA")
async def getWta():
    list = []
    documents = wta_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/wta/{item_id}", tags=["WTA"], description="Get WTA By ID", summary="Get WTA By ID")
async def getWtaById(item_id: int):
    existing_wta = wta_collections.find_one({"_id": item_id})
    if existing_wta is None:
        return {"message": f"wta with ID {item_id} not found."}
    else:
        return wta_collections.find_one({"_id": item_id})

@app.post("/wta/create", tags=["WTA"], description="Create New WTA", summary="Create New WTA")
async def createWta(ms: Wta, request: Request):
    try:
        wta_collections.insert_one({"_id": ms.id, "level": ms.level, "preset_value": ms.preset_value})
        return {"msg": "created successfully", "created_data": ms, "client": request.client}
    except:
        documents = wta_collections.find()
        for document in documents:
            id = document["_id"]
            if id == ms.id:
                return {"msg": {f"id {ms.id} already exist in fan, try using other id"}}

@app.put("/wta/update/{item_id}", tags=["WTA"], description="Update WTA By ID", summary="Update WTA By ID")
async def updateWta(wta: WtaPut, item_id: int):
    existing_wta = wta_collections.find_one({"_id": item_id})
    if existing_wta is None:
        return {"message": f"wta with ID {item_id} not found."}
    update_fields = {}
    if wta.level is not None:
        update_fields['level'] = wta.level
    if wta.preset_value is not None:
        update_fields['preset_value'] = wta.preset_value
    wta_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated to {update_fields}"}

@app.delete("/wta/delete/{item_id}", tags=["WTA"], description="Delete WTA By ID", summary="Delete WTA By ID")
async def deleteWta(item_id: int):
    existing_wta = wta_collections.find_one({"_id": item_id})
    if existing_wta is None:
        return {"message": f"wta with ID {item_id} not found."}
    else:
        wta_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

@app.get("/wta/log/all", tags=["WTA"], description="Get All wta Logs", summary="Get All wta Logs")
async def getAllwtaLog():
    device_list = []
    documents = wta_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/wta/log/create", tags=["WTA"], description="Create New wta Log", summary="Create New wta Log")
async def createwtaLog(devices: Log, request: Request):
    try:
        wta_details_log_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": devices.device_id,
                "status": devices.status,
                "timestamp": devices.timestamp,
                "updated_by": devices.updated_by
            }
        )
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        documents = wta_details_log_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == devices.device_id:
                return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}

@app.get("/wta/boardlog/all", tags=["WTA"], description="Get All wta Board Logs", summary="Get All wta Board Logs")
async def getAllBoardLog():
    device_list = []
    documents = wta_board_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list

@app.post("/wta/boardlog/create", tags=["WTA"], description="Create New wta Board Log", summary="Create New wta Board Log")
async def createwtaBoardLog(devices: Log, request: Request):
    try:
        wta_board_log_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": devices.device_id,
                "status": devices.status,
                "timestamp": devices.timestamp,
                "updated_by": devices.updated_by
            }
        )
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        documents = wta_board_log_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == devices.device_id:
                return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}

@app.get("/wta/details/all", tags=["WTA"], description="Get All wta Details", summary="Get All wta Details")
async def getwtaDetails():
    list = []
    documents = wta_details_collections.find()
    for document in documents:
        list.append(document)
    return list

@app.get("/wta/details/{item_id}", tags=["WTA"], description="Get wta Details By ID", summary="Get wta Details By ID")
async def getwtaDetailsById(item_id: int):
    existing_wta = wta_details_collections.find_one({"_id": item_id})
    if existing_wta is None:
        return {"message": f"wta with ID {item_id} not found."}
    else:
        return wta_details_collections.find_one({"_id": item_id})

@app.post("/wta/details/create", tags=["WTA"], description="Create New wta Details", summary="Create New wta Details")
async def createwtaDetails(devices: wtaDetails, request: Request):
    try:
        wta_details_collections.insert_one(
            {
                "_id": devices.id,
                "name": devices.name,
                "room": devices.room,
                "device_id": devices.device_id,
                "type": devices.type
            }
        )
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = wta_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}

@app.put("/wta/details/update/{item_id}", tags=["WTA"], description="Update wta Details By ID", summary="Update wta Details By ID")
def updatewtaDetailsById(device: wtaDetailsPut, item_id: int):
    existing_wta = wta_details_collections.find_one({"_id": item_id})
    if existing_wta is None:
        return {"message": f"wta with ID {item_id} not found."}
    update_fields = {}
    if device.name is not None:
        update_fields['name'] = device.name
    if device.room is not None:
        update_fields['room'] = device.room
    if  device.device_id is not None:
        update_fields['device_id'] = device.device_id
    if  device.type is not None:
        update_fields['type'] = device.type 
    wta_details_collections.update_one(
        {"_id": item_id},
        {"$set": update_fields}
    )
    return {"msg": f"updated device id {item_id} to {update_fields}"}

@app.delete("/wta/details/delete/{item_id}", tags=["WTA"], description="Delete wta Details By ID", summary="Delete wta Details By ID")
async def deletewtaDetailsById(item_id: int):
    existing_wta = wta_details_collections.find_one({"_id": item_id})
    if existing_wta is None:
        return {"message": f"wta with ID {item_id} not found."}
    else:
        wta_details_collections.delete_one({"_id": item_id})
        return {"msg": f"Successfully deleted item in {item_id}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8182, reload=True)