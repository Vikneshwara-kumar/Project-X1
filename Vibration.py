import RPi.GPIO as GPIO
import time

# Set up GPIO mode and pin
GPIO.setmode(GPIO.BCM)
vibration_pin = 17  # Use the appropriate GPIO pin number

# Set up the pin as input
GPIO.setup(vibration_pin, GPIO.IN)

try:
    while True:
        # Read the value from the vibration sensor
        vibration_value = GPIO.input(vibration_pin)
        
        if vibration_value == 1:
            print("Vibration detected!")
        else:
            print("No vibration.")
        
        time.sleep(1)  # Wait for a second before reading again

except KeyboardInterrupt:
    print("Monitoring stopped.")
    GPIO.cleanup()
