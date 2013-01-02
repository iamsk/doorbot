import RPi.GPIO as GPIO
import time

PORT = 7

def reset():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PORT, GPIO.IN)

def initcontroller():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PORT, GPIO.OUT)
    GPIO.output(PORT, True)

def open():
    GPIO.setup(PORT, GPIO.OUT)
    GPIO.output(PORT, False)
    time.sleep(2)
    GPIO.output(PORT, True)

