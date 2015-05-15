# -*- coding: utf-8 -*-  
# 有一个全局的计数num，每个线程获得这个计数器并做一些操作，然后将num+1
import threading
import time


class Mythread(threading.Thread):
	def run(self):
		global num
		num += 1
		time.sleep(0.002)
		msg = self.name+' set num to '+str(num)
		print (msg)


def test():
	global num
	for i in range(100):
		M=Mythread()
		M.start()
	return

if __name__ == '__main__':
	global num
	num = 0
	test()