# -*- coding: utf-8 -*-
# @Time    : 20-5-23 下午10:37
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : thread_pool.py
# @Software: PyCharm


from threading import Thread, current_thread
from queue import Queue
import time

class ThreadPool(object):
    def __init__(self, n):  # n 制定线程池内线程数
        self.q = Queue()   # 放任务的队列
        for i in range(n):
            Thread(target=self.worker, daemon=True).start()

    def worker(self):
        """一直去任务来实现的"""
        while True:
            func, args, kwargs = self.q.get()  # 取出任务
            func(*args, **kwargs)  # 运行任务
            self.q.task_done()  # 执行完毕,通知队列

    def put_q(self, func, *args, **kwargs):
        """放任务"""
        self.q.put((func, args, kwargs))

    def join_q(self):
        self.q.join()  # 阻塞等待完成


def task1():
    print('我是线程{},我正在执行task1'.format(current_thread().name))
    time.sleep(3)
    print('我是线程{},执行task1完毕'.format(current_thread().name))

def task2(*args, **kwargs):
    print('我是线程{},我正在执行task2'.format(current_thread().name))
    print('我接受的参数是', args, kwargs)
    time.sleep(3)
    print('我是线程{},执行task1完毕'.format(current_thread().name))

if __name__ == '__main__':
    pool = ThreadPool(2)
    pool.put_q(task1)
    pool.put_q(task2, args=(1, 2), kwargs={'A': 4, 'B': 7})
    pool.join_q()