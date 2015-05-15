# -*- coding: utf-8 -*-  
import threading
import time


class MyThread(threading.Thread):
	def run(self):
		global num
		if mutex.acquire(1):
			num += 1
			msg = self.name + ' set num to ' + str(num)
			print(msg)
			time.sleep(1)
			mutex.release()


mutex = threading.Lock()
num = 0


def test():
	for i in range(20):
		t = MyThread()
		t.start()
	return


if __name__ == '__main__':
	test()

