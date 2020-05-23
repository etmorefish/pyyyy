# -*- coding: utf-8 -*-
# @Time    : 20-5-23 下午10:04
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : thread_class.py
# @Software: PyCharm


import  time
from threading import Thread

class MyThread(Thread):
    def __init__(self, p_name):
        super().__init__()
        self.p_name = p_name

    def run(self):
        print('hello, {}'.format(self.p_name))
        time.sleep(3)
        print('bye')


my_thread = MyThread('fei')
my_thread.start()