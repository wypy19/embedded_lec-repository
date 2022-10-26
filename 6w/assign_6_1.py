import RPi.GPIO as GPIO
import time

SW = [5,6,13,19]
swVal = [0,0,0,0]
sw1value = []
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in SW: GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i in range(0,4):
            if(GPIO.input(SW[i])==1):
                swVal[i] += 1
                print('SW',i,'click',',',swVal[i])
        time.sleep(0.3)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
