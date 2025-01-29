FROM python:3.9-slim

WORKDIR /app

COPY subscriber.py /app/

RUN pip install paho-mqtt influxdb-client

CMD ["python", "subscriber.py"]
