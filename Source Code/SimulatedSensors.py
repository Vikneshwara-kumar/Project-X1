import random
import numpy as np
import datetime
from datetime import datetime as dt
from flowcontroller import FlowMeter

class TemperatureSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def generate_temperature(self):
        """
        Generates a simulated temperature value for the sensor and current time.

        Returns:
        A dictionary with the sensor ID, temperature value, and timestamp.
        """
        # Get the current time
        now = datetime.datetime.now()

        # Generate a random temperature value based on the time of day
        hour = now.hour
        if hour < 6 or hour > 20:
            # Nighttime, temperature is lower
            temperature = random.uniform(10.0, 15.0)
        elif hour < 10:
            # Morning, temperature is rising
            temperature = random.uniform(15.0, 20.0)
        elif hour < 16:
            # Midday, temperature is higher
            temperature = random.uniform(20.0, 30.0)
        else:
            # Afternoon/Evening, temperature is cooling down
            temperature = random.uniform(15.0, 20.0)

        # Create a dictionary with the sensor ID, temperature value, and timestamp
        data = {
            "sensor_id": self.sensor_id,
            "temperature": temperature,
            "timestamp": now.isoformat()
        }

        return data
    
class FlowSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def generate_Flow(self):
        """
        Generates a simulated flow value for the sensor and current time.

        Returns:
        A dictionary with the sensor ID, flow value, and timestamp.
        """

        # Input parameters
        diameter = 0.5 # m
        length = 10 # m
        density = 1000 # kg/m^3
        viscosity = 0.00089 # Pa*s

        flow_meter = FlowMeter(diameter, length, density, viscosity)

        # Get the current time
        now = datetime.datetime.now()

        # Generate a random Flow value based on the time of day
        hour = now.hour
        if hour < 6 or hour > 20:
            # Nighttime, pressure_drops is lower
            pressure_drops= random.uniform(5.0, 10.0) # kPa

            # Calculate flow rates and plot flow rate vs. pressure drop
            flow = flow_meter.plot_flow_rate(pressure_drops)
        elif hour < 10:
            # Morning, pressure_drops is rising
            pressure_drops = random.uniform(11.0, 30.0) # kPa
            # Calculate flow rates and plot flow rate vs. pressure drop
            flow =  flow_meter.plot_flow_rate(pressure_drops)
        elif hour < 16:
            # Midday, pressure_drops is higher
            pressure_drops = random.uniform(31.0, 60.0) # kPa
            # Calculate flow rates and plot flow rate vs. pressure drop
            flow = flow_meter.plot_flow_rate(pressure_drops)
        else:
            # Afternoon/Evening, pressure_drops is cooling down
            pressure_drops = random.uniform(61.0, 80.0) # kPa
            # Calculate flow rates and plot flow rate vs. pressure drop
            flow = flow_meter.plot_flow_rate(pressure_drops)

        # Create a dictionary with the sensor ID, flow value, and timestamp
        data = {
            "sensor_id": self.sensor_id,
            "flow": flow,
            "timestamp": now.isoformat()
        }

        return data

class PressureSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def generate_Flow(self):
        """
        Generates a simulated Pressure value for the sensor and current time.

        Returns:
        A dictionary with the sensor ID, flow value, and timestamp.
        """

        # Get the current time
        now = datetime.datetime.now()
        
        # Generate a random Flow value based on the time of day
        hour = now.hour
        if hour < 6 or hour > 20:
            # Nighttime, pressure_drops is lower
            pressure = random.uniform(5.0, 10.0) # kPa

        elif hour < 10:
            # Morning, pressure_drops is rising
            pressure = random.uniform(11.0, 30.0) # kPa

        elif hour < 16:
            # Midday, pressure_drops is higher
            pressure = random.uniform(31.0, 60.0) # kPa
        else:
            # Afternoon/Evening, pressure_drops is cooling down
            pressure = random.uniform(61.0, 80.0) # kPa

        timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        # Create a dictionary with the sensor ID, flow value, and timestamp
        data = {
            "sensor_id": self.sensor_id,
            "pressure": pressure,
            "timestamp": timestamp
        }

        return timestamp, self.sensor_id, pressure
