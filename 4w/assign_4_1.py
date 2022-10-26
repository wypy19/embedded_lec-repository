import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

GPIO.output(26,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(21,GPIO.LOW)
GPIO.output(20,GPIO.LOW)

while True:
    GPIO.output(16,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(16,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(21,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(20,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(20,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(26,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(26,GPIO.LOW)
    time.sleep(0.5)