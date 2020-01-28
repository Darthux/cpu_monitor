#!/usr/bin/python3
# this program is opened by cpu_monitor.py to check the CPU temperature
# Created by @Darthux

# the following 2 lines is not required unless you run this script stand alone
#from gpiozero import CPUTemperature
#from time import sleep
temp = CPUTemperature().temperature

# used to convert C to F
tempf = round((temp * 9/5) + 32)  # convert C to F

#print(round(temp))  # uncomment this for standalond testing
sleep(5)