import time
from socket import *

# set some vars here for ease of access
REDPIN = 17
WHITEPIN = 27
DEFPORT = 12000


# send out a message to the LEDs
# the input is a string where:
#   W = white on
#   w = white off
#   R = red on
#   r = red off
# repeat for reps times
def blink(message, reps=1, portnum=DEFPORT):
    print "[Info] Blinking " + message
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    addr = ("127.0.0.1", portnum)
    for i in range(reps):
        clientSocket.sendto(message, addr)
        time.sleep(5)


# access GPIO LEDs through UDP socket
def udpled(portnum=DEFPORT):
    # import here so that other programs don't need to be run
    # as sudo unless they are starting the server
    import RPi.GPIO as GPIO

    # set up GPIO
    GPIO.setup(REDPIN, GPIO.OUT)
    GPIO.setup(WHITEPIN, GPIO.OUT)
    GPIO.output(REDPIN, GPIO.LOW)
    GPIO.output(WHITEPIN, GPIO.LOW)

    # initialize socket
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', portnum))

    # listen for instructions
    while True:
        message, address = serverSocket.recvfrom(1024)
        # interpret message as a blink pattern
        for i in range(len(message)):
            if message[i] == "R":
                GPIO.output(REDPIN, GPIO.HIGH)
                time.sleep(0.2)
                continue
            if message[i] == "r":
                GPIO.output(REDPIN, GPIO.LOW)
                time.sleep(0.2)
                continue
            if message[i] == "W":
                GPIO.output(WHITEPIN, GPIO.HIGH)
                time.sleep(0.2)
                continue
            if message[i] == "w":
                GPIO.output(WHITEPIN, GPIO.LOW)
                time.sleep(0.2)
                continue
        # make sure to end with LEDs off
        GPIO.output(REDPIN, GPIO.LOW)
        GPIO.output(WHITEPIN, GPIO.LOW)
