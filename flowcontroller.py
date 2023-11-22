import math
import numpy as np

class FlowMeter:
    def __init__(self, diameter, length, density, viscosity):
        self.diameter = diameter
        self.length = length
        self.density = density
        self.viscosity = viscosity
    
    def calculate_flow_rate(self, pressure_drop):
        # Calculate Reynolds number
        velocity = math.sqrt((2 * pressure_drop * 1000) / self.density) # m/s
        reynolds_number = (self.density * velocity * self.diameter) / self.viscosity

        # Determine flow regime
        if reynolds_number < 2300:
            flow_regime = 'Laminar'
        elif reynolds_number > 4000:
            flow_regime = 'Turbulent'
        else:
            flow_regime = 'Transitional'

        # Calculate flow rate based on flow regime
        if flow_regime == 'Laminar':
            flow_rate = ((math.pi * pressure_drop * self.diameter**4) / (128 * self.viscosity * self.length)) * 3600 # m^3/h
        elif flow_regime == 'Turbulent':
            friction_factor = 0.25 / ((math.log10((0.25 / (3.7 * self.diameter)) + (5.74 / reynolds_number**0.9)))**2)
            flow_rate = ((math.pi * pressure_drop * self.diameter**2) / (4 * self.density * friction_factor)) * 3600 # m^3/h
        else:
            reynolds_crit = 2300 + ((4000 - 2300) / (math.log10(7) - math.log10(2)))
            if reynolds_number < reynolds_crit:
                flow_rate = ((math.pi * pressure_drop * self.diameter**4) / (128 * self.viscosity * self.length)) * 3600 # m^3/h
            else:
                friction_factor = 0.25 / ((math.log10((0.25 / (3.7 * self.diameter)) + (5.74 / reynolds_number**0.9)))**2)
                flow_rate = ((math.pi * pressure_drop * self.diameter**2) / (4 * self.density * friction_factor)) * 3600 # m^3/h

        return flow_rate
    
    def plot_flow_rate(self, pressure_drops):
        flow_rate = self.calculate_flow_rate(pressure_drops)
        return flow_rate

