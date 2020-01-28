# cpu_monitor
# CPU monitor and fan activation; check_temp.py required in the same directory.
# This script utilizes gpiosero to check the temperature of your RaspberryPi
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
