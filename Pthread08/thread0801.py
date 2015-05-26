# -*- coding: utf-8 -*-
import random
import threading
import time

__author__ = 'admin'


class MyThread(threading.Thread):
    def run(self):
        wait_time = random.randrange(10, 15)
        print('%s will wait %d seconds' % (self.name, wait_time))
        time.sleep(wait_time)
        print('%s finished!!!' % self.name)
        return


if __name__ == '__main__':
    print('main thread is waitting for exit ...')
    for i in range(5):
        t = MyThread()
        t.setDaemon(True)
        t.start()
    print('main thread finished!')
