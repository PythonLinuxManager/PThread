# -*- coding: utf-8 -*-  
import threading
import time


class Mythread(threading.Thread):
	def run(self):
		global num
		if mutex.acquire(1):
			num += 1
			time.sleep(0.1)
			msg = self.name + ' set num to ' + str(num)
			print(msg)
			mutex.acquire()
			mutex.release()
			mutex.release()
		return


num = 0
mutex = threading.RLock()
if __name__ == '__main__':
	for i in range(5):
		t = Mythread()
		t.start()