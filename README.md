# secure_iot_system

This project simulates an IoT system using containerized services for data communication, processing, storage, and visualization. The system uses Docker Compose to deploy services seamlessly.

## Features

- **Eclipse Mosquitto**: MQTT broker for device communication.
- **Publisher Service**: Simulates multiple IoT devices sending temperature and humidity data.
- **Subscriber Service**: Processes incoming data and stores it in InfluxDB.
- **InfluxDB**: Stores time-series data from IoT devices.
- **Grafana**: Visualizes data and generates alerts.
- **Alerts**: Configured in Grafana to notify on Discord when temperature exceeds thresholds.

## Quick Start

### Prerequisites

1. Docker and Docker Compose installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/Gent1b/secure_iot_system.git
   cd secure_iot_system
   ```

### Setup

1. **Environment Variables (`.env` file)**:
   - The `.env` file is already set up for using InfluxDB Cloud. However, if you want to adapt it to your own InfluxDB instance, you can change the values inside:
   ```
   INFLUXDB_URL=https://eu-central-1-1.aws.cloud2.influxdata.com
   INFLUXDB_TOKEN=<your-influxdb-token>
   INFLUXDB_ORG=secure_iot
   INFLUXDB_BUCKET=iot_data
   ```
   Replace `<your-influxdb-token>` with your own API token if needed.

2. **Start Services**:
   Build and start all services:
   ```bash
   docker-compose up --build
   ```

3. **Scale Publishers**:
   Simulate additional devices:
   ```bash
   docker-compose up --scale publisher_device=10
   ```
   This command scales the publisher devices to 10, meaning 10 virtual IoT devices will send data to the MQTT broker simultaneously.

### Access Services

- **Grafana Dashboard**: [http://localhost:3000](http://localhost:3000)
  - Default login: `admin` / `admin123`
- **InfluxDB**: [Visit InfluxDB (email for access)](https://eu-central-1-1.aws.cloud2.influxdata.com/orgs/07510f2d44eb892b)
- **Discord Alerts**: [Join Discord for alerts](https://discord.gg/ewaQGK4T)

## Architecture

1. **MQTT Broker**: Handles communication between IoT devices and the system.
2. **Publisher Devices**: Simulate IoT devices sending randomized temperature and humidity data.
3. **Subscriber**: Processes received data and stores it in InfluxDB.
4. **InfluxDB**: Stores IoT data in time-series format.
5. **Grafana**: Visualizes data and sends alerts.

## Notes

- To modify alert thresholds or dashboard configurations, edit the files under `./grafana/provisioning/alerts`.
- The `.env` file is included for ease of deployment, but credentials should not be exposed in production environments.

For additional details, contact me via email.

