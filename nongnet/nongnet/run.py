# -*- coding: utf-8 -*-
# @Time    : 19-7-16 下午3:58
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : run.py
# @Software: PyCharm


from scrapy.cmdline import execute

import time

if __name__ == '__main__':
    stime = time.time()
    execute('scrapy crawl nongnet_spider'.split(' '))
    etime = time.time()
    print('run time {}'.format(etime - stime))
