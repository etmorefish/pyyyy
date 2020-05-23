# -*- coding: utf-8 -*-
# @Time    : 20-5-22 下午5:04
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : datetime_rt.py
# @Software: PyCharm


# import  datetime
#
# d = datetime.date(2020, 5, 22)
# print(d)
#
# t = datetime.time(17, 5, 3, 50 )
# print(t)
#
# now = datetime.datetime.now()
# print(now)

from datetime import datetime

now = datetime.now()
print(now)
print(now.date())
print(now.time())

# datetime类中常用方法
# 1. 获取当前时间
now = datetime.now()
# 2.日期时间转化为时间戳
res = now.timestamp()
print(res)
# 3.时间戳转换为日期时间
res1 = datetime.fromtimestamp(res)
print(res1)
# 4.输出格式化
# print(res1.strftime('%Y年%m月%d日 %H: %'))
# 5.字符串砖时间
# Fri, 22 May 2020 17:16:25 GMT
a = '22 5 2020 17:16:25'
res2 = datetime.strptime(a, '%d %m %Y %H:%M:%S')
print(res2)

# 时间计算 timedelta
import datetime
now = datetime.datetime.now()
td  = datetime.timedelta(hours=5, minutes= 30, seconds=30, )
print(type(td))
print(now + td)
print(now - td)
# 两个时间日期的差值是<class 'datetime.timedelta'>对象

t