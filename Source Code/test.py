# temperature_humidity_monitor.py
import time
import Adafruit_DHT
from datetime import datetime

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
    # Define the DHT11 sensor type and GPIO pins for the DHT11 sensors and their respective sensor IDs
    DHT11_SENSOR_TYPE = Adafruit_DHT.DHT11
    temperature_sensor_pin = 4
    humidity_sensor_pin = 4
    temperature_sensor_id = "DHT11-Temperature-Sensor-01"
    humidity_sensor_id = "DHT11-Humidity-Sensor-01"

    # Initialize the TemperatureSensor and HumiditySensor classes
    temperature_sensor = TemperatureSensor(DHT11_SENSOR_TYPE, temperature_sensor_pin, temperature_sensor_id)
    humidity_sensor = HumiditySensor(DHT11_SENSOR_TYPE, humidity_sensor_pin, humidity_sensor_id)

    try:
        while True:
            # Read temperature and humidity from the sensors
            temperature_timestamp, temperature_sensor_id, temperature = temperature_sensor.read_temperature()
            humidity_timestamp, humidity_sensor_id, humidity = humidity_sensor.read_humidity()

            if temperature is not None:
                print(f"Temperature - Timestamp: {temperature_timestamp}, Sensor ID: {temperature_sensor_id}, Temperature: {temperature:.2f} °C")
            else:
                print("Failed to read temperature.")

            if humidity is not None:
                print(f"Humidity - Timestamp: {humidity_timestamp}, Sensor ID: {humidity_sensor_id}, Humidity: {humidity:.2f} %")
            else:
                print("Failed to read humidity.")

            time.sleep(2)
    except KeyboardInterrupt:
        print("Temperature and humidity monitoring stopped.")
