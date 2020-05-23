# -*- coding: utf-8 -*-
# @Time    : 20-5-23 下午9:33
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : thread_1.py
# @Software: PyCharm


# 进程:运行中的应用程序
# 线程:进程默认启动一个线程,叫主线程
# threading模块中提供了Thread, Lock, RLock, Condition等组件
'''
threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：

threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。

threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
'''

import  time
from threading import Thread

def f(p_name):
    print('hello f {}'.format(p_name))
    time.sleep(3)
    print('bye')

def f1():
    print('hello f1')
    time.sleep(3)
    print('bye')

if __name__ == '__main__':
    # f()
    # f1()
    # 实例化线程对象
    f_thread = Thread(target=f, args=('lei',), name='hello')
    f1_thread = Thread(target=f1)
    print('f_thread.getname:', f_thread.getName())
    f_thread.setName('hhhhhhhh')
    print('f_thread.getname2:', f_thread.getName())
    f_thread.setDaemon(True)  # 守护线程, 主线程结束后,程序结束
    f1_thread.setDaemon(True)
    f_thread.start()
    f1_thread.start()
    # f_thread.join()  # 主线程会等待1子线程执行完毕后在执行,反之
    # f1_thread.join()


    print('主线程执行完毕')