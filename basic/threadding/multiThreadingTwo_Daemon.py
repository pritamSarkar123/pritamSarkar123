#Daemon is kind of opposite to the Join
#we don't join the thread wnen Daemon is true
#by default daemon remains false
#we make it true when the thread has an infinite loop possibility
#Daemon terminates the thread associated with it, when main thread finishes
#irrespective of the thread has a infinite loop ongoing
import threading
import time

total=4

def incrementElementOne():
	global total
	for i in range(10): #finite iterator
		time.sleep(2)
		print('increment by one')
		total+=1
		print('increment by one completed')

def incrementElementTwo():
	global total
	for i in range(7): #finite iterator
		time.sleep(2)
		print('increment by two')
		total+=2
		print('increment by two completed')

def limitsElement():
	global total
	while True:
		if total>5:
			print('overload')
			total-=3
			print('3 substracted')
		else:
			time.sleep(1)
			print('waiting')

start=time.time()

creator1=threading.Thread(target=incrementElementOne,name='threadOne')
creator2=threading.Thread(target=incrementElementTwo,name='threadTwo')
limitor=threading.Thread(target=limitsElement,name='threadThree',daemon=True)

creator1.start()
creator2.start()
limitor.start()

creator1.join()
creator2.join()

end=time.time()

print(f'finishes after {end-start} sec , now total is {total}')