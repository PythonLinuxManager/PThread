# -*- coding: utf-8 -*-
import threading
import time


class MyThread(threading.Thread):
	def run(self):
		for i in range(10):
			print(self.name)
			time.sleep(0.001)
		return


if __name__ == '__main__':
	for i in range(20):
		MyThread().start()
