#!/usr/bin/python

from Adafruit_TSL2561 import Adafruit_TSL2561

# Initialise the sensor
LightSensor = Adafruit_TSL2561.Adafruit_TSL2651()

# Enable auto gain switching between 1x and 16x
# Default is False
LightSensor.enableAutoGain(True)

# Get the calculated lux value, this is a spot reading so if you're under light
# lux = Adafruit_TSL2561.calculateLux()


