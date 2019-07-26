# -*- coding: utf-8 -*-
# @Time    : 19-7-16 下午3:16
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : cccsv.py
# @Software: PyCharm
'''
如果想修改列与列之间的分隔符，可以传入delimiter参数
writer = csv.writer(csvfile,delimiter=' ')
可以调用writerows()方法写入多行
writer。writerows（[[],[],[]]）

'''
import csv
with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['1001','Mike',20])
    writer.writerow(['1002','Bob',22])
    writer.writerow(['1003','Jordan',21])
