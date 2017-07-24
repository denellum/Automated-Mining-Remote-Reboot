#!/usr/bin/python

# V-1.0 
# Script to Ping a server, if no response hard
# power it down, and wait a set time and power
# it back on.
# Authors - denellum, tsurk, hanner

# Libraries to import
import RPi.GPIO as GPIO
import time
import os
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Init list with pin numbers
pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# Loop through all pins and set to 'Low'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Sleep variables
SleepSHUTDOWN = 6 # I set to 6 just incase, 5 is really only needed.
SleepSTART = 1    # Just needs a quick 'press' to turn it back on.
SleepWAIT = 10    # I like 10 seconds...

# Server List - Just do one per line
Server1 = "10.4.2.11"

# Server-1 - Main loop
response = os.system("ping -qc 5 " + Server1)

if response == 0:
  print bcolors.OKGREEN + "Server-1, is up!" + bcolors.ENDC
else:
  print bcolors.FAIL + "Server-1, is down!" + bcolors.ENDC
  try:
    time.sleep(SleepWAIT);
    GPIO.output(2, GPIO.LOW)
    print bcolors.WARNING + "Server-1, being powered off..." + bcolors.ENDC
    time.sleep(SleepSHUTDOWN);
    print bcolors.WARNING + "Server-1, is powered off!" + bcolors.ENDC
    GPIO.output(2, GPIO.HIGH)
    time.sleep(SleepWAIT);
    print bcolors.WARNING + "Server-1, being powered on..." + bcolors.ENDC
    GPIO.output(2, GPIO.LOW)
    time.sleep(SleepSTART);
    GPIO.output(2, GPIO.HIGH)
    print bcolors.WARNING + "Server-1, is powered on!" + bcolors.ENDC
	

  # End program cleanly with keyboard
  except KeyboardInterrupt:
    print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

  # End program cleanly with keyboard || This is buggy for some reason
  #except KeyboardInterrupt:
    #print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
# End main loop
