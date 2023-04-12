from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["localSmartHomeServer"]

device_collections = db["devices"]
device_detail_collections = db["devices_detail"]
device_details_log_collections = db["devices_details_logs"]
device_board_log_collections = db["devices_board_logs"]

fan_collections = db["fan"]
fan_details_collections = db["fan_details"]
fan_details_log_collections = db["fan_details_logs"]
fan_board_log_collections = db["fans_board_logs"]

led_collections = db["led"]
led_details_collections = db["led_details"]
led_details_log_collections = db["led_details_logs"]

mechanics_collections = db['Mechanics']
mechanics_details_collections = db['Mechanics_details']
mechanics_details_log_collections = db['Mechanics_details_logs']

eb_sensor_collections = db["eb_sensor"]
eb_status_collections = db["eb_status"]

eb_ups_voltage_collections = db["eb_ups_voltage"]
eb_ups_ampere_collections = db["eb_ups_ampere"]

eb3phasae_sensor_collections = db["eb3_sensor"]
eb3phasae_voltage_collections = db["eb3_voltage"]
eb3phasae_ampere_collections = db["eb3_ampere"]

board_log_collections = db["board_logs"]
room_collections = db["room"]
temp_collections = db["temperature"]

motionsensor_collections = db["motion_sensor"]
motionsensor_details_collections = db["motion_sensor_details"]

wta_collections = db["wta"]
wta_details_log_collections = db["wta_details_logs"]
wta_board_log_collections = db["wta_board_logs"]
wta_details_collections = db["wta_sensor_details"]