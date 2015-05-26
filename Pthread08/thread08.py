# -*- coding: utf-8 -*-
import random
import threading
import time

__author__ = 'admin'


class Mythread(threading.Thread):
    def run(self):
        wait_time = random.randrange(1, 10)
        print('%s will wait %d seconds ' % (self.name, wait_time))
        time.sleep(wait_time)
        print('%s finished!!!' % self.name)
        return


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = Mythread()
        t.start()
        threads.append(t)
    print('main thread is waiting for exit')
    for t in threads:
        t.join(1)
    print('main thread finished')
