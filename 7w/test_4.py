import threading
import serial
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gdata = ""

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
            if(gdata.find('13') >= 0):
                gdata = ""
                print("left")
            elif(gdata.find('6') >= 0):
                gdata = ""
                print("right")
            elif(gdata.find('5') >= 0):
                gdata = ""
                print("go")
            elif(gdata.find('19') >= 0):
                gdata = ""
                print("back")
            elif(gdata.find('stop') >= 0):
                gdata = ""
                print("stop")
                

    except KeyboardInterrupt:
        pass


if __name__=="__main__":

    task1=threading.Thread(target=serial_thread)
    task1.start()
    main()
    bleSerial.close()
    