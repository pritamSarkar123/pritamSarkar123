#Events used to communicate between multiple threades,using a common switch/flag ,one thread update it another reacts on it
import threading
import time
import numpy as np
event=threading.Event()
def flag():
    time.sleep(3)
    event.set()
    print('Event is set')
    time.sleep(7)
    event.clear()
    print("Event is cleared")
    
def start_operations():
    event.wait()
    while event.is_set():
        print("starting random integer task")
        x=np.random.randint(1,30)
        time.sleep(.5)
        if x==29:
            print("true")
        print("Event complete")
t1=threading.Thread(target=flag)
t2=threading.Thread(target=start_operations)

t1.start()
t2.start()
