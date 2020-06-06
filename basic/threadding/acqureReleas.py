import threading
lock=threading.Lock()
COUNT=1000
x=0
def add_2():
    global x
    lock.acquire()
    for i in range(COUNT):
        x+=2
    lock.release()
            
def add_3():
    global x
    lock.acquire()
    for i in range(COUNT):
        x+=3
    lock.release()
            
def sub_4():
    global x
    lock.acquire()
    for i in range(COUNT):
        x-=4
    lock.release()
            
def sub_1():
    global x
    lock.acquire()
    for i in range(COUNT):
        x-=1
    lock.release()
            
t1=threading.Thread(target=add_2)
t2=threading.Thread(target=add_3)
t3=threading.Thread(target=sub_4)
t4=threading.Thread(target=sub_1)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("It ends with x={}".format(x))