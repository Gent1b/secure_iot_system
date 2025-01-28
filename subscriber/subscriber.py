import paho.mqtt.client as mqtt
import json
import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# MQTT broker details
BROKER = os.getenv("BROKER", "mqtt_broker")
PORT = 1883
TOPIC = "iot/devices"

# InfluxDB details
INFLUXDB_URL = os.getenv("INFLUXDB_URL", "http://influxdb:8086")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN", "strongpassword123")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG", "secure_iot")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET", "iot_data")

# InfluxDB client setup
client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

def on_message(client, userdata, msg):
    """Callback when a message is received from MQTT."""
    try:
        data = json.loads(msg.payload.decode())
        print(f"Received data: {data}")

        # Write data to InfluxDB
        point = Point("sensor_data") \
            .tag("device_id", data["device_id"]) \
            .field("temperature", data["temperature"]) \
            .field("humidity", data["humidity"])
        write_api.write(bucket=INFLUXDB_BUCKET, record=point)
        print(f"Data written to InfluxDB: {data}")
    except Exception as e:
        print(f"Error processing message: {e}")

def main():
    # MQTT client setup
    mqtt_client = mqtt.Client()
    mqtt_client.on_message = on_message

    mqtt_client.connect(BROKER, PORT, 60)
    mqtt_client.subscribe(TOPIC)

    print("Subscriber is listening...")
    mqtt_client.loop_forever()

if __name__ == "__main__":
    main()
