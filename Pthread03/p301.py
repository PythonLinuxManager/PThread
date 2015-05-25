# -*- coding: utf-8 -*-
import threading

'''
死锁：
	有两个锁，MA和MB
	有两个资源，RA和RB
	两锁嵌套，相互依赖，则随机产生死锁
	伪码如下，线程数量越多越容易产生死锁
	function1(
	ma.acquire
	mb.acquire
	mb.release
	ma.release
	)
	function2(
	mb.acquire
	ma.acquire
	ma.release
	mb.release
	)
	run(
	function1()
	function2()
	)

	多线程中锁的原因是线程并不按顺序来执行，哪个线程得到CPU就执行，如果情况类似如下代码，则一定会产生死锁
	每个方法正常执行，但多线程时，一个线程do1把MA锁定，另一个线程do2把mb锁定，然后都等待另一个锁release，死锁产生


'''
ma = threading.RLock()
mb = threading.RLock()
ra = 0
rb = 0


class MyThread(threading.Thread):
    def do1(self):
        if ma.acquire():
            msg = self.name + 'DO1-->\tMA.acquire()'
            print(msg)
            if mb.acquire(1):
                msg = self.name + 'DO1-->\tMB.acquire()'
                print(msg)
                mb.release()
                print('DO1-->-b-b-b--b-b-b-b--b-b-b-b-b-b-b-b')
            ma.release()
            print('DO1-->-a-a-a-a-a-a-a-a-a-a-a-a-a')
        return

    def do2(self):
        if mb.acquire():
            msg = self.name + 'DO2-->\tMB.acquire()'
            print(msg)
            if ma.acquire(1):
                msg = self.name + 'DO2-->\tMA.acquire()'
                print(msg)
                ma.release()
                print('DO2-->-a-a-a-a-a-a-a-a-a-a-a-a-a')
            mb.release()
            print('DO2-->-b-b-b--b-b-b-b--b-b-b-b-b-b-b-b')
        return

    def run(self):
        self.do1()
        self.do2()
        return


def test():
    for i in range(100):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()
