import serial
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

try:
    while True:
        sendData = " I'm raspberry \r\n"
        bleSerial.write( sendData.encode())
        time.sleep(1.0)
        
        data = bleSerial.readline()
        print(data)
        
except KeyboardInterrupt:
    pass

bleSerial.close()