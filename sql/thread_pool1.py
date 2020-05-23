# -*- coding: utf-8 -*-
# @Time    : 20-5-23 下午11:05
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : thread_pool1.py
# @Software: PyCharm

from multiprocessing.pool import ThreadPool
from threading import Thread, current_thread
from queue import Queue
import time




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
    pool.apply_async(task1)
    pool.apply_async(task2,  args=(1, 2), kwds={'A': 4, 'B': 7})
    print("任务提交完毕")
    # pool.terminate()  # 终止所有任务,终止线程池
    pool.close()   # 必须在join钱添加close
    pool.join()
    print("所有任务完成")