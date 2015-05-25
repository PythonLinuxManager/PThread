import threading
import time
import queue


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            for i in range(100):
                if queue.qsize() > 1000:
                    pass
                else:
                    count = count + 1
                    msg = 'Production of the product ' + str(count)
                    print(msg)
                    queue.put(msg)
            time.sleep(1)
        return


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            for i in range(3):
                if queue.qsize() < 100:
                    pass
                else:
                    msg = self.name + 'consumer ' + queue.get()
                    print(msg)
            time.sleep(1)
        return


queue = queue.Queue()


def test():
    for i in range(500):
        queue.put('init pro ' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()


if __name__ == '__main__':
    test()
