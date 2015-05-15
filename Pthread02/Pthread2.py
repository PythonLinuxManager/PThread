# -*- coding: utf-8 -*-  
# 有一个全局的计数num，每个线程获得这个计数器并做一些操作，然后将num+1
# 没有锁机制时，下面代码会有问题，num值 不定，拿到的信息不同
import threading
import time


class Mythread(threading.Thread):
	def run(self):
		global num
		mutex.acquire()  # 加锁就ok,注意要把锁定区域定下
		num += 1
		time.sleep(0.002)
		msg = self.name + ' set num to ' + str(num)
		print(msg)
		mutex.release()


def test():
	global num
	for i in range(100):
		M = Mythread()
		M.start()
	return


if __name__ == '__main__':
	global num
	mutex = threading.Lock()
	num = 0
	test()