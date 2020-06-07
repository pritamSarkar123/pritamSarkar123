import threading
import time
event = threading.Event()
def sleeper():
	event.set()
	time.sleep(10)
	event.clear()
	print("sleep complete")

def accessor():
	event.wait()
	while event.is_set():
		time.sleep(0.2)
		print("Sleeper sleeping ZzZzZ..")

t1=threading.Thread(target=sleeper,name="thread1")
t2=threading.Thread(target=accessor,name="thread2")

t1.start()
t2.start()

t1.join()
t2.join()


