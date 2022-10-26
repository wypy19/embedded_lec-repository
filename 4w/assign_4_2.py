import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinNum = (26,16,21,20)

for i in pinNum: GPIO.setup(i,GPIO.OUT)
for i in pinNum: GPIO.output(i,GPIO.LOW)

try:
    while True:
        for i in pinNum:
            GPIO.output(i,GPIO.HIGH)
            time.sleep(1.0)
            GPIO.output(i,GPIO.LOW)
            time.sleep(0.5)

except: 
    for i in pinNum: GPIO.output(i,GPIO.LOW)
