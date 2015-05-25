# coding:utf-8
import threading
import time

'''
    多线程里生产者与消费者问题
    1.使用Condition类型的锁
        增加了wait,notify方法
'''


class Producer(threading.Thread):
    def run(self):
        global count

        while True:
            if con.acquire():
                if count > 1000:
                    con.wait()
                else:
                    count = count + 100
                    msg = self.name + 'Poduce 100,Count=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(1)
        return


class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 1000:
                    con.wait()
                else:
                    count = count - 300
                    msg = self.name + 'Consumer 300,count=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(1)
        return


count = 500
con = threading.Condition()


def test():
    for i in range(4):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
    return


if __name__ == '__main__':
    test()
