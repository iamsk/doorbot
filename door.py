import RPi.GPIO as GPIO
import time

PORT = 7


def open():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PORT, GPIO.OUT)
    GPIO.output(PORT, False)
    time.sleep(2)
    GPIO.setup(PORT, GPIO.IN)

