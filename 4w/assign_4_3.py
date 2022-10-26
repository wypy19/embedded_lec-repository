import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)

pinNum = (26,16,21,20)
ledOrder = [random.choice(pinNum) for i in range(0,10)]

for i in pinNum: GPIO.setup(i,GPIO.OUT)
for i in pinNum: GPIO.output(i,GPIO.LOW)

print(ledOrder)

try:
    for i in ledOrder:
            GPIO.output(i,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(i,GPIO.LOW)
            time.sleep(0.5)

except: 
    for i in pinNum: GPIO.output(i,GPIO.LOW)
