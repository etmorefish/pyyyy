# -*- coding: utf-8 -*-
# @Time    : 20-2-18 下午4:35
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : demo.py
# @Software: PyCharm


# 让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可以执行

def f():
    print(__name__)

if __name__ == '__main__':
    f()