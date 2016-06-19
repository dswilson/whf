# Copyright (c) 2016 Dave Wilson
#
# This is the state controller for an array of 16 relays, controlled by an MCP23017 i2c breakout chip.
# It uses the AdaFruit GPIO library:  https://github.com/adafruit/Adafruit_Python_GPIO
# Only ten relays have a purpose at this time, but we manage all 16 because discrete outputs do not
# seem to be well behaved at this time (sending any output can impact the state of all relays).  We
# don't need to be providing power to the coils on unused relays.
#
# These relays are active low, so a boolean FALSE will send current through the coil, and a boolean
# TRUE will turn them off.
#
# 1 = furnace lockout (normally closed)
# 2 = fan damper power (apply power for 90 secs to fully open damper, leave power 
# on while fan is in operation - it has a spring closure)
# 3 = fan power (use in conjunction with one of the three fan speeds)
# 4 = fan low (left hand potentiometer) (transition here after running in max for 
# at least one second)
# 5 = fan medium (right hand potentiometer) (transition here after running in max 
# for at least one second)
# 6 = fan max (zero impedance)
# 7 = downstairs zone clockwise (damper open)
# 8 = downstairs zone counter clockwise (damper close)
# 9 = upstairs zone clockwise (damper open)
# 10 = upstairs zone counter clockwise (damper close)
# 
# Apply current for 90 seconds to completely open or close either of the zone dampers. 
#
# Imports

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.MCP230xx as MCP

# Global variables.  We'll have a couple of constants and a shared array that defines the
# current state of the relay array.

on = FALSE
off = TRUE
global outputs = {0:off,1:off,2:off,3:off,4:off,5:off,6:off,7:off,8:off,9:off,10:off,11:off,12:off,13:off,14:off,15:off,16:off}

class stateControl(MCP.MCP23017):

def initialize():
  global outputs = {0:off,1:off,2:off,3:off,4:off,5:off,6:off,7:off,8:off,9:off,10:off,11:off,12:off,13:off,14:off,15:off,16:off}
  self.output_pins(outputs)
  
