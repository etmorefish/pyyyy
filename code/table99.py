# -*- coding: utf-8 -*-
# @Time    : 19-6-21 下午6:21
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : table99.py
# @Software: PyCharm

class PrintTable(object):
    def __init__(self):
        print('开始打印99乘法表')
        self.print99()

    def print99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('%dx%d=%2d'%(j,i,i*j),end=' ')
            print('\n')

if __name__ == '__main__':
    p = PrintTable()