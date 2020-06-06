#when u have multiple thread functions to run using a loop,
#when all having a sleep like delaying statement or code
#first start them all in one loop
#then join them all in another loop, after sleep is being called
import threading
import time

def sleeper(n,name):
	print(f'{name} is going to sleep for {n} seconds')
	time.sleep(n)
	print(f'{name} woke up')

thread_list=[]
start=time.time()
for i in range(5):
	t=threading.Thread(target=sleeper,
		name=f"thread{i}",
		args=(5,f"thread{i}"))
	thread_list.append(t)
	thread_list[-1].start()
	time.sleep(0.2)

for t in thread_list: #joining forward order
	t.join()



# reversed_thread_list=thread_list[::-1]
# for t in reversed_thread_list:
# 	t.join()
end=time.time()
print(f'{end-start} sec time taken')