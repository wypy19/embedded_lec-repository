import RPi.GPIO as GPIO
import time
import serial
import threading

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)
gdata = ""
SW = [5, 6, 13, 19]

msg = ['Go', 'TurnRight', 'TurnLeft', 'Back']
PWMA1, PWMA2 = 18, 23
AIN1, AIN2 = 22, 27
BIN1, BIN2 = 25, 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA1, GPIO.OUT)
GPIO.setup(PWMA2, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
for i in SW:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
L_Motor = GPIO.PWM(PWMA1, 500)
R_Motor = GPIO.PWM(PWMA2, 500)
L_Motor.start(0)
R_Motor.start(0)

def move(x):
    if (x == 13):
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
        GPIO.output(BIN1, 0)
        GPIO.output(BIN2, 1)
        L_Motor.ChangeDutyCycle(5)
        R_Motor.ChangeDutyCycle(30)
    elif (x == 6):
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
        GPIO.output(BIN1, 0)
        GPIO.output(BIN2, 1)
        L_Motor.ChangeDutyCycle(30)
        R_Motor.ChangeDutyCycle(5)
    elif (x == 5):
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
        GPIO.output(BIN1, 0)
        GPIO.output(BIN2, 1)
        L_Motor.ChangeDutyCycle(30)
        R_Motor.ChangeDutyCycle(30)
    elif (x == 19):
        GPIO.output(AIN1, 1)
        GPIO.output(AIN2, 0)
        GPIO.output(BIN1, 1)
        GPIO.output(BIN2, 0)
        L_Motor.ChangeDutyCycle(30)
        R_Motor.ChangeDutyCycle(30)
    elif (x == 'stop'):
        L_Motor.ChangeDutyCycle(0)
        R_Motor.ChangeDutyCycle(0)

def makecircle():
    for i in range(10):
        if i % 2 == 0:
            move(13)
        else:
            move(5)
        time.sleep(0.2)





def serial_thread():
    global gdata
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gdata = data


def main():
    global gdata
    try:
        while True:
            if (gdata.find('13') >= 0):
                gdata = ""
                print("left")
                move(13)
            elif (gdata.find('6') >= 0):
                gdata = ""
                print("right")
                move(6)
            elif (gdata.find('5') >= 0):
                gdata = ""
                print("go")
                move(5)
            elif (gdata.find('19') >= 0):
                gdata = ""
                print("back")
                move(19)
            elif (gdata.find('stop') >= 0):
                gdata = ""
                print("stop")
                move('stop')
            elif (gdata.find('cir') >= 0):
                gdata = ""
                print("make circle")
                makecircle()

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    task1 = threading.Thread(target=serial_thread)
    task1.start()
    main()
    bleSerial.close()
    GPIO.cleanup()
