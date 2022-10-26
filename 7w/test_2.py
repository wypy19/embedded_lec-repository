from ast import Num
import threading
import time

def print_cube(num):
    print("Cube : ", num*num*num)
    time.sleep(3.0)

def print_square(num):
    print("square : ", num*num)
    time.sleep(5.0)

if __name__=="__main__":
    t1=threading.Thread(target=print_square, args=(10,))
    t2=threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")