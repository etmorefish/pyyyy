# -*- coding: utf-8 -*-
# @Time    : 20-5-23 下午10:11
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : thread_lock.py
# @Software: PyCharm

from threading import Thread, Lock

lock = Lock()

a = 0

def addd():
    global a
    lock.acquire()
    for i in range(1000000):
        a += 1
    lock.release()
        # '''
        # a += 1
        # 1. x = a +1
        # 2. a = x
        # '''

def redu():
    global a
    lock.acquire()
    for i in range(1000000):
        a -= 1
    lock.release()

        # '''
        # 初始值: a = 0
        # t1: x1 = a + 1   # x1 = 1
        # t2: x2 = a - 1   # x2 = -1
        # t2: a = x2       # a = -1
        # t1: a = x1       # a = 1
        # '''

if __name__ == '__main__':
    t1 = Thread(target=addd)
    t2 = Thread(target=redu)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(a)
    # addd()
    # redu()
    # print(a)  # 0