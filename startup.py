#!/usr/bin/python2

import RPi.GPIO as GPIO
import os
import time
import signal
import subprocess

def log(mes):
    print mes


# things to do on boot
def startup():
    log("[Message] Starting datalogger")

    # begin the datalogger process
    return subprocess.Popen(['/usr/bin/python3 /home/pi/telemetry/datalogger.py | /usr/bin/python2 /home/pi/telemetry/sender.py'], shell=True)


# things to do on shutdown
def shutdown(pgrp):
    # kill the datalogger process
    os.killpg(os.getpgid(pgrp.pid), signal.SIGTERM)

    # cleanup GPIO
    GPIO.cleanup()

    # shutdown
    log("[Message] Shutting down now!")
    os.system("sudo shutdown -h now")
    exit(0)


# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)
log("[Message] Initiated inputs and outputs")

# Set shutdown handler
GPIO.add_event_detect(24, GPIO.FALLING, callback=shutdown, bouncetime=300)

# start logger
pgrp = startup()

# kill time
try:
    while(True):
        time.sleep(1000)
except:
    GPIO.cleanup()
exit(0)
