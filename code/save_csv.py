#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-12 18:37:40
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import  csv
output_list = ['1','2','3','4']
output_list1 = ['a','b','c','d']

with open('test1.csv','a+',encoding='UTF-8',newline='') as csvfile:
	w = csv.writer(csvfile)
	w.writerow(output_list1)
	w.writerow(output_list)

# with open('test.csv','r',encoding='UTF-8') as csvfile:
# 	csv_reader = csv.reader(csvfile)
# 	for row in csv_reader:
# 		print(row)




