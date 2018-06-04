import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.output(20, 1)

for x in range(200):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(.0010)
    GPIO.output(21, GPIO.LOW)
    time.sleep(.0010)

GPIO.cleanup()
