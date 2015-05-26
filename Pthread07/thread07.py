# -*- coding: utf-8 -*-
__author__ = 'admin'

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadName, event):
        threading.Thread.__init__(self, name=threadName)
        self.threadEvent = event
        return

    def run(self):
        print('%s is ready' % self.name)
        self.threadEvent.wait()
        print('%s run !' % self.name)
        return


sinal = threading.Event()

for i in range(10):
    t = MyThread(str(i), sinal)
    t.start()
time.sleep(3)
sinal.set()
