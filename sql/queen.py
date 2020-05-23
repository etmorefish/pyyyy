# -*- coding: utf-8 -*-
# @Time    : 20-5-23 下午10:27
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : queen.py
# @Software: PyCharm


from threading import Thread
from queue import Queue
from random import randint

# 创建队列长度
q = Queue(10)

def f(q):
    for x in range(10):
        num = randint(0, 1000)
        q.put(num)

def f1(q):
    for y in range(5):
        num = q.get()
        print(num)


# t1 = Thread(target=f, args=(q,))
# t2 = Thread(target=f1, args=(q,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
q.put(1)
print(q.qsize())
q.get(1)
print(q.empty())
q.put(1)
q.put(1)
q.put(1)
q.put(1)
print(q.full())
q.task_done()
q.task_done()
q.task_done()
q.task_done()
q.task_done()