from SimulatedSensors import TemperatureSensor
from SimulatedSensors import FlowSensor
from SimulatedSensors import PressureSensor
import json
import time

def main():
    sensor = TemperatureSensor(sensor_id="sensor-01")
    data1 = sensor.generate_temperature()
    sensor2 = FlowSensor(sensor_id="sensor-02")
    data2 = sensor2.generate_Flow()
    sensor3 = PressureSensor(sensor_id="sensor-03")
    data3 = sensor3.generate_Flow()

    data = {
            "sensor-1": data1,
            "sensor-2": data2,
            "sensor-3": data3        
        }

    jmsg = json.dumps(data, indent=4)
    print(jmsg)

while True:
    main()
    time.sleep(5)
