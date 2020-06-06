import threading
import time
import queue
q=queue.Queue()
lock=threading.Lock()

x=0
def putting(n):
    global x
    with lock:
        while x<n:
            print("waiting to put")
            time.sleep(1)
            print("element put")
            q.put(x)
            x+=1
def getting():
    while not q.empty():
        print("waiting to get")
        time.sleep(2)
        print(q.get())

thread1=threading.Thread(target=putting,args=(5,),name="thread1")
thread2=threading.Thread(target=getting,name="thread2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Atlast x= {x}")