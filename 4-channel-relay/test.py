import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.HIGH)

GPIO.output(2, GPIO.LOW)
time.sleep(2)

GPIO.cleanup()
