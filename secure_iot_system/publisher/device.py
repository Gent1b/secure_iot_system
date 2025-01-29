import paho.mqtt.client as mqtt
import random
import time
import os
import json

BROKER = os.getenv("BROKER", "mqtt_broker")
PORT = 1883
TOPIC = os.getenv("MQTT_TOPIC", "iot/devices")

DEVICE_ID = os.getenv("HOSTNAME", "device_default")

def generate_sensor_data():
    """Generate random sensor data with occasional spikes."""
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 60.0), 2)

    # Introduce a spike with a 10% probability
    if random.random() < 0.1:
        temperature += random.uniform(10.0, 20.0) * random.choice([-1, 1])
        humidity += random.uniform(10.0, 20.0) * random.choice([-1, 1])

    return {
        "device_id": DEVICE_ID,
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2),
    }

def publish_data():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 120)

    while True:
        data = generate_sensor_data()
        json_data = json.dumps(data)  
        client.publish(TOPIC, json_data)
        print(f"Published: {json_data}")
        time.sleep(30)

if __name__ == "__main__":
    print(f"Starting device with ID: {DEVICE_ID}")
    publish_data()
