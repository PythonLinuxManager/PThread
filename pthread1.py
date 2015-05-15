# -*- coding: utf-8 -*-  
import threading
import time


class MThread(threading.Thread):
	def run(self):
		for i in range(3):
			time.sleep(0.5)
			msg = "I'm " + self.name + '@' + str(i)
			print(msg)


def test():
	for i in range(5):
		t = MThread()
		t.start()


if (__name__ == '__main__'):
	test()