import RPi.GPIO as GPIO
import time

SW = [5,6,13,19]
BUZZER = 12

def tone(x):
    pulse = 0
    if(x == 5): pulse = 262
    elif(x==6): pulse = 394
    elif(x==13): pulse = 330
    elif(x==19): pulse = 349
    p.ChangeFrequency(pulse)
    p.start(50)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in SW: GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER,GPIO.OUT)
p = GPIO.PWM(BUZZER,261)

try:
    while True:
        for i in range(0,4):
            if(GPIO.input(SW[i])==1):
                print('SW',i,'click')
                tone(SW[i])
                while(GPIO.input(SW[i])==1): continue
        p.stop()
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
