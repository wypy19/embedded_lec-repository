import RPi.GPIO as GPIO
import time

SW = [5,6,13,19]
msg = ['Go','TurnRight','TurnLeft','Back']
PWMA1,PWMA2=18,23
AIN1,AIN2=22,27
BIN1,BIN2=25,24

def move(x):
    if(x==13):
        GPIO.output(AIN1,1)
        GPIO.output(AIN2,0)
        GPIO.output(BIN1,0)
        GPIO.output(BIN2,1)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        
    elif(x==6):
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        GPIO.output(BIN1,1)
        GPIO.output(BIN2,0)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        
    elif(x==5):
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        GPIO.output(BIN1,0)
        GPIO.output(BIN2,1)
        L_Motor.ChangeDutyCycle(60)
        R_Motor.ChangeDutyCycle(60)
        
    elif(x==19):
        GPIO.output(AIN1,1)
        GPIO.output(AIN2,0)
        GPIO.output(BIN1,1)
        GPIO.output(BIN2,0)
        L_Motor.ChangeDutyCycle(60)
        R_Motor.ChangeDutyCycle(60)

    elif(x=='stop'):        
        L_Motor.ChangeDutyCycle(0)
        R_Motor.ChangeDutyCycle(0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA1,GPIO.OUT)
GPIO.setup(PWMA2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)

for i in SW: GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
L_Motor=GPIO.PWM(PWMA1,500)
R_Motor=GPIO.PWM(PWMA2,500)
L_Motor.start(0)
R_Motor.start(0)

try:
    while True:
        for i in range(0,4):
            if(GPIO.input(SW[i])==1):
                print(msg[i])
                move(SW[i])
                while(GPIO.input(SW[i])==1): continue
        move('stop')
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()