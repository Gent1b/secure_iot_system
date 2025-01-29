import requests
import os

INFLUXDB_URL = os.getenv("INFLUXDB_URL")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")

def check_health():
    headers = {"Authorization": f"Token {INFLUXDB_TOKEN}"}
    try:
        response = requests.get(f"{INFLUXDB_URL}/health", headers=headers, timeout=5)
        if response.status_code == 200:
            print("Cloud InfluxDB is healthy!")
        else:
            print(f"Cloud InfluxDB health check failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Health check error: {e}")

if __name__ == "__main__":
    check_health()
