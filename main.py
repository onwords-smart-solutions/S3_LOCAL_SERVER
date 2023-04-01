import time
from fastapi import FastAPI, Request
from models import *
from mongo import *
import uvicorn

app = FastAPI(title="Onwords Local Smart Home Server", docs_url="/admin", redoc_url="/document")


@app.get("/device", tags=["Devices"])
async def getAllDevices():
    device_list = []
    documents = device_collections.find()
    print('inside try')
    print('doc ', documents)
    for document in documents:
        device_list.append(document)
    return device_list


@app.get("/device/details", tags=["Devices"])
async def getAllDeviceDetails():
    device_list = []
    documents = device_detail_collections.find()
    for document in documents:
        device_list.append(document)
    return device_list


@app.get("/device/log", tags=["Devices"])
async def getAllDeviceLog():
    device_list = []
    documents = device_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list


@app.get("/device/boardlog", tags=["Devices"])
async def getAllBoardLog():
    device_list = []
    documents = device_board_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list


@app.get("/device/{item_id}", tags=["Devices"])
async def getDeviceById(item_id: int):
    return device_collections.find_one({"_id": item_id})


@app.get("/device/details/{item_id}", tags=["Devices"])
async def getDeviceDetailsById(item_id: int):
    return device_detail_collections.find_one({"_id": item_id})


@app.put("/device/details/{item_id}", tags=["Devices"])
def updateDeviceDetailsById(device: Devices_details_Put, item_id: int):
    device_detail_collections.update_one(
        {"_id": item_id},
        {"$set":{
            "name": device.name,
            "room": device.room,
            "device_id": device.device_id,
            "type": device.type
            }
        }
    )
    return {"msg": f"updated device id {item_id} to {device}"}


@app.delete("/device/details/{item_id}", tags=["Devices"])
async def deleteDeviceDetailsById(item_id: int):
    device_detail_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.delete("/device/{item_id}", tags=["Devices"])
async def deleteDeviceById(item_id: int):
    device_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/device/{item_id}", tags=["Devices"])
def updateDeviceById(device: Devices_put, item_id: int):
    device_collections.update_one({"_id": item_id}, {"$set": {"status": device.status}})
    return {"msg": f"updated device id {item_id} to {device.status}"}


@app.post("/device", tags=["Devices"])
async def createDevice(devices: Devices, request: Request):
    try:
        device_collections.insert_one({"_id": devices.id, "status": devices.status})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = device_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/device/details", tags=["Devices"])
async def createDeviceDetails(devices: Devices_details, request: Request):
    try:
        device_detail_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = device_detail_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/device/log", tags=["Devices"])
async def createDeviceLog(devices: Log, request: Request):
    try:
        device_details_log_collections.insert_one(
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
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.post("/device/boardlog", tags=["Devices"])
async def createDeviceBoardLog(devices: Log, request: Request):
    try:
        device_board_log_collections.insert_one(
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
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.get("/fan", tags=["Fan"])
async def getAllFans():
    fan_list = []
    documents = fan_collections.find()
    for document in documents:
        fan_list.append(document)
    return fan_list


@app.get("/fan/{item_id}", tags=["Fan"])
async def getFanById(item_id: int):
    return fan_collections.find_one({"_id": item_id})


@app.delete("/fan/{item_id}", tags=["Fan"])
async def deleteFanById(item_id: int):
    fan_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/fan/{item_id}", tags=["Fan"])
def updateFanById(device: Fan_put, item_id: int):
    fan_collections.update_one({"_id": item_id}, {"$set": {"status": device.status, "speed": device.speed}})
    return {"msg": f"updated device id {item_id} to {device.status} and speed to{device.speed}"}


@app.post("/fan", description="Create a new item", tags=["Fan"])
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


@app.get("/fans/details", tags=["Fan"])
async def getFanDetails():
    try:
        device_list = []
        documents = fan_details_collections.find()
        for document in documents:
            device_list.append(document)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"

@app.get("/fans/details/{item_id}", tags=["Fan"])
async def getFanDetailsById(item_id: int):
    return fan_details_collections.find_one({"_id": item_id})

@app.get("/fans/log", tags=["Fan"])
async def getFanLog():
    device_list = []
    documents = fan_details_log_collections.find()
    for x in documents:
        device_list.append(x)

    return device_list


@app.post("/fan/details", tags=["Fan"])
async def createFanDetails(devices: Fan_details, request: Request):
    try:
        fan_details_collections.insert_one(
            {
                "_id": devices.id,
                "name": devices.device_name,
                "room": devices.room,
                "device_id": devices.device_id,
                "type": devices.type
            }
        )
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = fan_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/fan/log", tags=["Fan"])
async def createFanLog(devices: Log, request: Request):
    try:
        fan_details_log_collections.insert_one(
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
        return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}


@app.get("/fans/boardlog", tags=["Fan"])
async def getFanBoardLog():
    try:
        device_list = []
        documents = fan_board_log_collections.find()
        for x in documents:
            device_list.append(x)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"

@app.post("/fan/boardlog", tags=["Fan"])
async def createFanBoardLog(devices: Log, request: Request):
    try:
        fan_board_log_collections.insert_one(
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
        return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}



@app.get("/led", tags=["LED"])
async def getLed():
    list = []
    documents = led_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/led/{item_id}", tags=["LED"])
async def getLedById(item_id: int):
    return led_collections.find_one({"_id": item_id})


@app.delete("/led/{item_id}", tags=["LED"])
async def deleteLedById(item_id: int):
    led_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/led/{item_id}", tags=["LED"])
def updateLedById(led: Led_put, item_id: int):
    led_collections.update_one({"_id": item_id}, {"$set": {"brightness": led.brightness, "status": led.status, "R": led.R, "G": led.G, "B": led.B}})
    return {"msg": f"updated to {led}"}


@app.post("/led", description="Create a new LED", tags=["LED"])
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


@app.get("/leds/details", tags=["LED"])
async def getLedDetails():
    try:
        device_list = []
        documents = led_details_collections.find()
        for document in documents:
            device_list.append(document)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"

@app.get("/leds/details/{item_id}", tags=["LED"])
async def getLedDetailsById(item_id: int):
    return led_details_collections.find_one({"_id": item_id})

@app.get("/leds/log", tags=["LED"])
async def getLedLog():
    device_list = []
    documents = led_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list


@app.post("/leds/details", tags=["LED"])
async def getLedDetails(devices: Led_details, request: Request):
    try:
        led_details_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = led_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/leds/log", tags=["LED"])
async def getLedLog(devices: Log, request: Request):
    try:
        led_details_log_collections.insert_one(
            {"_id": time.time(), "device_id": devices.device_id, "status": devices.status,
             "timestamp": devices.timestamp, "updated_by": devices.updated_by})
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.get("/mechanics", tags=["Mechanics"])
async def getMechanics():
    list = []
    documents = mechanics_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/mechanics/{item_id}", tags=["Mechanics"])
async def getMechanicsById(item_id: int):
    return mechanics_collections.find_one({"_id": item_id})


@app.delete("/mechanics/{item_id}", tags=["Mechanics"])
async def deleteMechanicsById(item_id: int):
    mechanics_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/mechanics/{item_id}", tags=["Mechanics"])
def updateMechanicsById(mechanics: Mechanics_put, item_id: int):
    mechanics_collections.update_one({"_id": item_id}, {"$set": {"values": mechanics.values}})
    return {"msg": f"updated to {mechanics}"}


@app.post("/mechanics", description="Create a new Mechanics", tags=["Mechanics"])
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


@app.get("/mechanic/details", tags=["Mechanics"])
async def getMechanicsDetails():
    device_list = []
    documents = mechanics_details_collections.find()
    for document in documents:
        device_list.append(document)
    return device_list


@app.get("/mechanic/detail/{item_id}", tags=["Mechanics"])
async def getMechanicsDetailsById(item_id: int):
    return mechanics_details_collections.find_one({"_id": item_id})


@app.get("/mechanic/log", tags=["Mechanics"])
async def getMechanicsLog():
    device_list = []
    documents = mechanics_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list


@app.post("/mechanic/details", tags=["Mechanics"])
async def createMechanicsDetails(devices: Mechanics_details, request: Request):
    try:
        mechanics_details_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = mechanics_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/mechanic/log", tags=["Mechanics"])
async def createMechanicsLog(devices: Log, request: Request):
    try:
        mechanics_details_log_collections.insert_one(
            {"_id": time.time(), "device_id": devices.device_id, "status": devices.status,
             "timestamp": devices.timestamp, "updated_by": devices.updated_by})
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.get("/eb", tags=["EB"])
async def getEb():
    list = []
    documents = eb_sensor_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb/{item_id}", tags=["EB"])
async def getEbById(item_id: int):
    return eb_sensor_collections.find_one({"_id": item_id})


@app.delete("/eb/{item_id}", tags=["EB"])
async def deleteEbById(item_id: int):
    eb_sensor_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/eb/{item_id}", tags=["EB"])
def updateEbById(eb: Eb_put, item_id: int):
    eb_sensor_collections.update_one(
        {"_id": item_id}, {
            "$set": {
                "voltage": eb.voltage,
                "amp": eb.amp,
                "ups_voltage": eb.ups_voltage,
                "ups_amp": eb.ups_AMP,
                "status": eb.status,
                "ups_battery_percentages": eb.ups_battery_percentage
            }
        }
    )
    return {"msg": f"updated to {eb}"}


@app.post("/eb", description="Create a new Mechanics", tags=["EB"])
async def createEb(eb: Eb, request: Request):
    try:
        eb_sensor_collections.insert_one(
            {
                "_id": eb.id,
                "voltage": eb.voltage,
                "amp": eb.amp,
                "ups_voltage": eb.ups_voltage,
                "ups_amp": eb.ups_AMP,
                "status": eb.status,
                "ups_battery_percentages": eb.ups_battery_percentage
            }
        )
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_sensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/eb/status", tags=["EB"])
async def getEbStatus():
    list = []
    documents = eb_status_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb/status/{item_id}", tags=["EB"])
async def getEbStatusById(item_id: int):
    return eb_status_collections.find_one({"_id": item_id})


@app.post("/eb/status", description="Create a new Mechanics", tags=["EB"])
async def createEbStatus(eb: EbStatus, request: Request):
    try:
        eb_status_collections.insert_one({"_id": eb.id, "status": eb.status, "time_stamp": eb.time_stamp})
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_status_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/ups/voltage", tags=["EB"])
async def getUpsVoltage():
    list = []
    documents = eb_ups_voltage_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/ups/voltage/{item_id}", tags=["EB"])
async def getUpsVoltageById(item_id: int):
    return eb_ups_voltage_collections.find_one({"_id": item_id})


@app.post("/ups/voltage", description="Create a new Mechanics", tags=["EB"])
async def createUpsVoltage(eb: UpsVoltage, request: Request):
    try:
        eb_ups_voltage_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": eb.device_id,
                "voltage": eb.voltage,
                "time_stamp": eb.time_stamp
            }
        )
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_ups_voltage_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/ups/ampere", tags=["EB"])
async def getUpsAmpere():
    list = []
    documents = eb_ups_ampere_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/ups/ampere/{item_id}", tags=["EB"])
async def getUpsAmpereById(item_id: int):
    return eb_ups_ampere_collections.find_one({"_id": item_id})


@app.post("/ups/ampere", description="Create a new Mechanics", tags=["EB"])
async def createUpsAmpere(eb: UpsAmpere, request: Request):
    try:
        eb_ups_ampere_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": eb.device_id,
                "ampere": eb.ampere,
                "time_stamp": eb.time_stamp
            }
        )
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_ups_ampere_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/eb3", tags=["EB 3 Phase"])
async def getEb3():
    list = []
    documents = eb3phasae_sensor_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb3/{item_id}", tags=["EB 3 Phase"])
async def getEb3ById(item_id: int):
    return eb3phasae_sensor_collections.find_one({"_id": item_id})


@app.delete("/eb3/{item_id}", tags=["EB 3 Phase"])
async def deleteEb3ById(item_id: int):
    eb3phasae_sensor_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/eb3/{item_id}", tags=["EB 3 Phase"])
def updateEb3ById(eb3: Eb3_put, item_id: int):
    eb3phasae_sensor_collections.update_one(
        {"_id": item_id}, {
            "$set": {
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

            }
        }
    )
    return {"msg": f"updated to {eb3}"}


@app.post("/eb3", description="Create a new Mechanics", tags=["EB 3 Phase"])
async def createEb3(eb3: Eb3, request: Request):
    try:
        eb3phasae_sensor_collections.insert_one(
            {
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
            }
        )
        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_sensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb3.id:
                return {"msg": {f"id {eb3.id} already exist in fan, try using other id"}}


@app.get("/eb3/voltage/", tags=["EB 3 Phase"])
async def getEb3Voltage():
    list = []
    documents = eb3phasae_voltage_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb3/voltage/{item_id}", tags=["EB 3 Phase"])
async def getEb3VoltageById(item_id: int):
    return eb3phasae_voltage_collections.find_one({"device_id": item_id})


@app.post("/eb3/voltage", description="Create a new Mechanics", tags=["EB 3 Phase"])
async def createEb3Voltage(eb3: Eb3Voltage, request: Request):
    try:
        eb3phasae_voltage_collections.insert_one(
            {
                "_id": time.time(), 
                "device_id": eb3.device_id,
                "r_voltage": eb3.r_voltage,
                "y_voltage": eb3.y_voltage,
                "b_voltage": eb3.b_voltage,
                "time_stamp": eb3.time_stamp
            }
        )

        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_voltage_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == eb3.device_id:
                return {"msg": {f"id {eb3.device_id} already exist in fan, try using other id"}}


@app.put("/eb3/voltage/{item_id}", tags=["EB 3 Phase"])
def updateEb3VoltageById(eb3: Eb3Voltage, item_id: int):
    eb3phasae_voltage_collections.update_one(
        {"device_id": item_id}, {
            "$set": {
                "r_voltage": eb3.r_voltage,
                "y_voltage": eb3.y_voltage,
                "b_voltage": eb3.b_voltage,
                "time_stamp": eb3.time_stamp
            }
        }
    )
    return {"msg": f"updated to {eb3}"}

@app.get("/eb3/ampere/", tags=["EB 3 Phase"])
async def getEb3Ampere():
    list = []
    documents = eb3phasae_ampere_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb3/ampere/{item_id}", tags=["EB 3 Phase"])
async def getEb3AmpereById(item_id: int):
    return eb3phasae_ampere_collections.find_one({"device_id": item_id})


@app.post("/eb3/ampere", description="Create a new Mechanics", tags=["EB 3 Phase"])
async def createEb3Ampere(eb3: Eb3Ampere, request: Request):
    try:
        eb3phasae_ampere_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": eb3.device_id,
                "r_ampere": eb3.r_ampere,
                "y_ampere": eb3.y_ampere,
                "b_ampere": eb3.b_ampere,
                "time_stamp": eb3.time_stamp
            }
        )

        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_ampere_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb3.id:
                return {"msg": {f"id {eb3.id} already exist in fan, try using other id"}}

@app.put("/eb3/ampere/{item_id}", tags=["EB 3 Phase"])
def updateEb3AmpereById(eb3: Eb3Ampere, item_id: int):
    eb3phasae_ampere_collections.update_one(
        {"device_id": item_id}, {
            "$set": {
                "r_ampere": eb3.r_ampere,
                "y_ampere": eb3.y_ampere,
                "b_ampere": eb3.b_ampere,
                "time_stamp": eb3.time_stamp
            }
        }
    )
    return {"msg": f"updated to {eb3}"}


@app.get("/room", tags=["Rooms"])
async def getRoom():
    room_list = []
    documents = room_collections.find()
    for document in documents:
        room_list.append(document)
    return room_list

@app.post("/room", description="Create a new room", tags=["Rooms"])
async def createRoom(room: Rooms, request: Request):
    try:
        room_collections.insert_one(
            {
                "_id": room.id,
                "name": room.name,
                "device_id": room.devices,
                "fan_id": room.fan,
                "led_id": room.led,
                "mechanics_id": room.mechanics,
                "motion_sensor_id": room.motion_sensor
            }
        )
        return {"msg": "created successfully", "created_data": room, "client": request.client}
    except:
        documents = device_collections.find()
        for document in documents:
            id = document["_id"]
            if id == room.id:
                return {"msg": {f"id {room.id} already exist in rooms, try using other id"}}

@app.get("/room/{item_id}", tags=["Rooms"])
async def getRoomById(item_id: int):
    return room_collections.find_one({"_id": item_id})

@app.put("/room/{item_id}", tags=["Rooms"])
async def updateRoomById(rooms: Rooms, item_id: int):
    eb3phasae_ampere_collections.update_one(
        {"_id": item_id}, {
            "$set": {
                "name": rooms.name,
                "device_id": rooms.devices,
                "fan_id": rooms.fan,
                "led_id": rooms.led,
                "mechanics_id": rooms.mechanics,
                "motion_sensor_id": rooms.motion_sensor
            }
        }
    )
    return {"msg": f"updated to {rooms}"}

@app.delete("/room/{item_id}", tags=["Rooms"])
async def deleteRoomById(item_id: int):
    room_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.get("/temp", tags=["Temperature"])
async def getTemp():
    room_list = []
    documents = temp_collections.find()
    for document in documents:
        room_list.append(document)
    return room_list


@app.post("/temp", description="Create a new item", tags=["Temperature"])
async def createTemp(temp: Temperature, request: Request):
    try:
        temp_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": temp.device_id,
                "room": temp.room,
                "temperature": temp.temperature,
                "humidity": temp.humidity,
                "timestamp": temp.timestamp
            }
        )
        return {"msg": "created successfully", "created_data": temp, "client": request.client}
    except:
        documents = temp_collections.find()
        for document in documents:
            id = document["_id"]
            if id == temp.device_id:
                return {"msg": {f"id {temp.device_id} already exist in temp, try using other id"}}

# to run use this command uvicorn main:app --reload --host 0.0.0.0 --port 8182


@app.get("/motionsensor", tags=["Motion Sensor"])
async def getMotionsensor():
    list = []
    documents = motionsensor_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/motionsensor/{item_id}", tags=["Motion Sensor"])
async def getMotionsensorById(item_id: int):
    return motionsensor_collections.find_one({"_id": item_id})


@app.delete("/motionsensor/{item_id}", tags=["Motion Sensor"])
async def deleteMotionsensor(item_id: int):
    motionsensor_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/motionsensor/{item_id}", tags=["Motion Sensor"])
async def updateMotionsensor(motion: MotionSensor_Put, item_id: int):
    motionsensor_collections.update_one(
        {"_id": item_id},
        {"$set": {
            "ss": motion.ss,
            "on_s": motion.on_s,
            "off_s": motion.off_s,
            "time": motion.time
        }})
    return {"msg": f"updated to {motion}"}


@app.post("/motionsensor", description="Create a new MotionSensor", tags=["Motion Sensor"])
async def createMotionsensor(ms: MotionSensor, request: Request):
    try:
        motionsensor_collections.insert_one({"_id": ms.id, "ss": ms.ss, "on_s": ms.on_s, "off_s": ms.off_s, "time": ms.time})
        return {"msg": "created successfully", "created_data": ms, "client": request.client}
    except:
        documents = motionsensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == ms.id:
                return {"msg": {f"id {ms.id} already exist in fan, try using other id"}}

@app.get("/motionsensors/details", tags=["Motion Sensor"])
async def getMotionsensorDetails():
    list = []
    documents = motionsensor_details_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/motionsensor/details/{item_id}", tags=["Motion Sensor"])
async def getMotionsensorDetailsById(item_id: int):
    return motionsensor_details_collections.find_one({"_id": item_id})


@app.post("/motionsensor/details", tags=["Motion Sensor"])
async def createMotionsensorDetails(devices: MotionSensor_details, request: Request):
    try:
        motionsensor_details_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = motionsensor_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.put("/motionsensor/details/{item_id}", tags=["Motion Sensor"])
def updateMotionsensorDetailsById(device: MotionSensor_details_put, item_id: int):
    motionsensor_details_collections.update_one(
        {"_id": item_id},
        {
            "$set":{
                "name": device.device_name,
                "room": device.room,
                "device_id": device.device_id,
                "type": device.type
            }
        }
    )

    return {"msg": f"updated device id {item_id} to {device}"}

@app.delete("/motionsensor/details/{item_id}", tags=["Motion Sensor"])
async def deleteMotionsensorDetailsById(item_id: int):
    motionsensor_details_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.get("/temp", tags=["Temperature"])
async def getTemp():
    room_list = []
    documents = temp_collections.find()
    for document in documents:
        room_list.append(document)
    return room_list


@app.post("/temp", description="Create a new item", tags=["Temperature"])
async def createTemp(temp: Temperature, request: Request):
    try:
        temp_collections.insert_one(
            {
                "_id": temp.device_id,
                "ss": temp.device_id,
                "on_s": temp.room,
                "off_s": temp.temperature,
                "time": temp.humidity,
            }
        )
        return {"msg": "created successfully", "created_data": temp, "client": request.client}
    except:
        documents = temp_collections.find()
        for document in documents:
            id = document["_id"]
            if id == temp.device_id:
                return {"msg": {f"id {temp.device_id} already exist in temp, try using other id"}}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8182, reload=True)