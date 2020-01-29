# !/usr/bin/env python3
# CPU monitor and fan activation; check_temp.py required in the same directory.
# This script utilizes gpiozero to check the temperature of your RaspberryPi
# every 5 seconds and will toggle a fan on or off based on the result.
# I'm sure theres a better way to do this without 2 files but I'm not that smart.
# All pins are BCM not physical.
# Requires a PN2222 transistor, a 5v capable fan and 4 GPIO (2 being ground)

################################# How to hook up ################################
#                               Attach FAN+ to 5v                               #
#                                                                               #
#                                 PN2222 Pinout                                 #
#                                 _____________                                 #
#                                 1     2     3                                 #
#                                 |     |     |                                 #
#                                GND  GPIO   FAN-                               #
#                                                                               #
#################################################################################

# Created by @Darthux

from gpiozero import CPUTemperature, OutputDevice
from time import sleep

# comment out the line below to use F instead of C
temp = CPUTemperature().temperature  # naming the actual temp

# uncomment the line below if you want to use F instead of C
#temp = round((CPUTemperature().temperature * 9/5) + 32)  # convert C to F
fan = OutputDevice(21)  # Physical pin 40
hot = 65    # when to turn the fan on
while True:
    exec(open("check_temp.py").read())  # this file has a 5 second delay in it
    if temp >= hot:
        fan.on()
    else:
        fan.off()
