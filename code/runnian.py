# -*- coding: utf-8 -*-
# @Time    : 19-7-1 下午8:29
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : runnian.py
# @Software: PyCharm
#
a= 0
for i in range(2000,3001):
    if (i%4==0 and i%100!=0) or i%400==0:
        a +=1
        print(i,end=" ")
        if(a%10==0):
            print("\n")