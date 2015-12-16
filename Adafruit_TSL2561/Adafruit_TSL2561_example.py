#!/usr/bin/python

from Adafruit_TSL2561 import AdafruitTSL2561

# Initialise the sensor
LightSensor = AdafruitTSL2561()

# Enable auto gain switching between 1x and 16x
# Default is False
LightSensor.enable_auto_gain(True)

# Get the calculated lux value, this is a spot reading so if you're under light
try:
    lux = LightSensor.calculate_lux()
except OverflowError as e:
    print(e)
else:
    print('Lux value is %d', lux)
