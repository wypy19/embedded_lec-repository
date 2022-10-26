import threading
import os
import time

def task1():
    print("Task 1 assigned to thread: ",threading.current_thread().name)
    print("ID of process running task 1: ", os.getpid())
    a=1
    while True:
        print('thread 1')
        time.sleep(1.0)
        a=a+1
        if a > 10: break

def task2():
    print("Task 2 assigned to thread: ",threading.current_thread().name)
    print("ID of process running task 2: ", os.getpid())
    a=1
    while True:
        print('thread 2')
        time.sleep(1.0)
        a=a+1
        if a > 5: break
        
if __name__=="__main__":

    print("ID of process running main program", os.getpid())

    print("Main thread name: ", threading.main_thread().name)

    t1=threading.Thread(target=task1, name='t1')
    t2=threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")