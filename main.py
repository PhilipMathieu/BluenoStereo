#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import time
import threading
import udpled
import subprocess


# things to do on boot
def startup():
    print "[Message] Welcome to Blueno Stereo"

    # start the LED server
    thread = threading.Thread(target=udpled.udpled, args=())
    thread.daemon = True
    thread.start()

    udpled.blink("WwWwWw")

    # begin the security logger
    subprocess.call("/home/pi/.virtualenvs/cv/bin/python security.py", shell=True)

    GPIO.cleanup()
    exit(0)


# things to do on shutdown
def shutdown(channel):
    # release GPIO
    GPIO.cleanup()
    print "[Message] Shutting down now!"
    os.system("sudo shutdown -h now")
    exit(0)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)
print("[Info] Telling Sleepy Pi we are running pin 25")

# Set shutdown handler
GPIO.add_event_detect(24, GPIO.RISING, callback=shutdown, bouncetime=300)

startup()

try:
    while(True):
        time.sleep(1000)
except:
    GPIO.cleanup()
exit(0)
