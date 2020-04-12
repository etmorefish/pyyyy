# -*- coding: utf-8 -*-
# @Time    : 20-4-9 下午7:08
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : ac1.py
# @Software: PyCharm

'''
有一个很经典的问题是，当前时间是aa:bb,请问若干分钟后是什么时间？我们今天的问题是一个相反的问题。

已知现在的时刻是星期x的yy:zz时刻，请问n分钟前是周几，时间是多少。

例如现在是周三，02:10,则200分钟之前，应该是周二，22:50。
样例输入
3
02:10
200    3   20
样例输出
2
22:50
'''
import sys
d = int(input())
now = input()
n = int(input())    # 60000

h = int(now.split(':')[0])  #  2
m = int(now.split(':')[1])  # 10

ms = n - n//60 * 60  #20   0
hs = n // 60    # 3   1000
ds = hs //24   # 0    41

if ms>m:
    mm = m + 60 - ms
    hh = h + 23 - hs
    if hs> h:
        print('{}'.format(d-ds-1))
    print('{}:{}'.format(hh,mm))
else:
    mm = m - ms
    hour = hs - hs//24 * 24  # 16
    days =  hs // 24 // 7  # 5
    hh = h + 24 - hour
    if hs> h:
        print('{}'.format((d+7-days)-1))
    print('{}:{}'.format(hh,mm))