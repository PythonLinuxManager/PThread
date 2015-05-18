# -*- coding: utf-8 -*-
import threading
import time

'''
死锁：
	有两个锁，MA和MB
	有两个资源，RA和RB

'''
ma = threading.RLock()
mb = threading.RLock()
ra = 0
rb = 0


class MyThread(threading.Thread):
	def do1(self):
		if ma.acquire():
			msg = self.name + '操作资源A'
			print(msg)
			if mb.acquire(1):
				msg = self.name + '操作资源B'
				print(msg)
				mb.release()
			ma.release()
		return

	def do2(self):
		if mb.acquire():
			msg = self.name + '操作资源B'
			print(msg)
			if ma.acquire(1):
				msg = self.name + '操作资源A'
				print(msg)
				ma.release()
			mb.release()
		return

	def run(self):
		self.do1()
		self.do2()
		return


def test():
	for i in range(500):
		t = MyThread()
		t.start()


if __name__ == '__main__':
	test()