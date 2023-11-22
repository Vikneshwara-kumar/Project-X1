# temperature_humidity_monitor.py
from SimulatedSensors import PressureSensor
import json
import time
import Adafruit_DHT
from datetime import datetime
import math
import paho.mqtt.client as mqtt


class TemperatureSensor:
    def __init__(self, sensor_type, sensor_pin, sensor_id):
        self.sensor_type = sensor_type
        self.sensor_pin = sensor_pin
        self.sensor_id = sensor_id

    def read_temperature(self):
        try:
            humidity, temperature_celsius = Adafruit_DHT.read_retry(self.sensor_type, self.sensor_pin)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return timestamp, self.sensor_id, temperature_celsius
        except RuntimeError as e:
            print("Error:", str(e))
            return None, None, None

class HumiditySensor:
    def __init__(self, sensor_type, sensor_pin, sensor_id):
        self.sensor_type = sensor_type
        self.sensor_pin = sensor_pin
        self.sensor_id = sensor_id

    def read_humidity(self):
        try:
            humidity, temperature_celsius = Adafruit_DHT.read_retry(self.sensor_type, self.sensor_pin)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return timestamp, self.sensor_id, humidity
        except RuntimeError as e:
            print("Error:", str(e))
            return None, None, None


if __name__ == "__main__":

    # Define the GPIO pins for the DHT11 sensors and their respective sensor IDs (you can modify these values accordingly)
    DHT11_SENSOR_TYPE = Adafruit_DHT.DHT11
    temperature_sensor_pin = 4
    humidity_sensor_pin = 4
    temperature_sensor_id = "TI01"
    humidity_sensor_id = "HI01"

    # Initialize the TemperatureSensor and HumiditySensor classes
    temperature_sensor = TemperatureSensor(DHT11_SENSOR_TYPE, temperature_sensor_pin, temperature_sensor_id)
    humidity_sensor = HumiditySensor(DHT11_SENSOR_TYPE, humidity_sensor_pin, humidity_sensor_id)
    pressure_sensor = PressureSensor(sensor_id="PI100")

    mqtt_broker_host = "192.168.1.119"
    mqtt_broker_port = 1883  # Default MQTT port
    mqtt_topic = "sensors/data"  # MQTT topic to publish data

    # Initialize MQTT client
    mqtt_client = mqtt.Client()

    # Connect to the MQTT broker
    mqtt_client.connect(mqtt_broker_host, mqtt_broker_port)

    try:
        while True:
            # Read temperature and humidity from the sensors
            temperature_timestamp, temperature_sensor_id, temperature = temperature_sensor.read_temperature()
            temperature_data = {
            "timestamp": temperature_timestamp,
            "sensor_id": temperature_sensor_id,
            "Temperature": temperature
            }
            humidity_timestamp, humidity_sensor_id, humidity = humidity_sensor.read_humidity()
            humidity_data = {
            "timestamp": humidity_timestamp,
            "sensor_id": humidity_sensor_id,
            "Humidity": humidity
            }
            pressure_timestamp, pressure_sensor_id, pressure = pressure_sensor.generate_Flow()
            pressure_data = {
            "timestamp": pressure_timestamp,
            "sensor_id": pressure_sensor_id,
            "Pressure":  math.ceil(pressure) 
            }

            if temperature is not None:
                print(f"Temperature - Timestamp: {temperature_timestamp}, - Sensor ID: {temperature_sensor_id}, - Temperature: {temperature:.2f} °C")
            else:
                print("Failed to read temperature.")
                temperature_data = {}

            if humidity is not None:
                print(f"Humidity - Timestamp: {humidity_timestamp}, - Sensor ID: {humidity_sensor_id}, - Humidity: {humidity:.2f} %")
            else:
                print("Failed to read humidity.")
                humidity_data = {}
            
            if pressure is not None:
                print(f"Pressure - Timestamp: {pressure_timestamp}, - Sensor ID: {pressure_sensor_id}, - Pressure: {pressure:.2f} %")
            else:
                print("Failed to read pressure.")
                pressure_data = {}

        
            data = {
                "sensor-1": temperature_data,
                "sensor-2": humidity_data,  
                "sensor-3": pressure_data          
            }
            jmsg = json.dumps(data, indent=4)
            print(jmsg)

            # Publish JSON data to MQTT broker
            mqtt_client.publish(mqtt_topic, payload=jmsg)

            time.sleep(1)

    except KeyboardInterrupt:
        print("Sensor monitoring stopped.")


    
