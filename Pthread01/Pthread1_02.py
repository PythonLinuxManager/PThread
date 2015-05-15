# -*- coding: utf-8 -*-
import threading
import time


class MYThread(threading.Thread):
	def run(this):
		for i in range(30):
			time.sleep(0.001)
			print(this.name)
		return


if __name__ == '__main__':
	for i in range(30):
		MYThread().start()