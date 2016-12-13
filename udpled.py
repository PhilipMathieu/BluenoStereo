import time
from socket import *

REDPIN = 17
WHITEPIN = 27
DEFPORT = 12000


# send out a message to the LEDs
def blink(message, reps=1, portnum=DEFPORT):
    print "[Info] Blinking " + message
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    addr = ("127.0.0.1", portnum)
    for i in range(reps):
        clientSocket.sendto(message, addr)
        time.sleep(5)


# simple script for testing that the output is working
def socktest(portnum=DEFPORT):
    while True:
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(1)
        message = 'RWrwRWrw'
        addr = ("127.0.0.1", portnum)
        clientSocket.sendto(message, addr)
        time.sleep(5)


# access GPIO LEDs through UDP socket
def udpled(portnum=DEFPORT):
    import RPi.GPIO as GPIO
    # start udp access to LEDs
    GPIO.setup(REDPIN, GPIO.OUT)
    GPIO.setup(WHITEPIN, GPIO.OUT)
    GPIO.output(REDPIN, GPIO.LOW)
    GPIO.output(WHITEPIN, GPIO.LOW)
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', portnum))
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
        GPIO.output(REDPIN, GPIO.LOW)
        GPIO.output(WHITEPIN, GPIO.LOW)