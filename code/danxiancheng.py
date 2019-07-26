#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 18:30:12
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$

import time
import requests

link_list = []
# with open('alexa.txt','r') as file:
# 	file_list = file.readlines()
# 	# print(file_list)
# 	with open('alexas.txt','w')as f:
# 		for eachone in file_list:
# 			eachone = 'http://www.'+eachone
# 			f.write(eachone)
# 			print(eachone)
	
# 简单的单线程抓取网页
with open('testtime.txt','r')as flie:
	file_list = flie.readlines()
	for eachone in file_list:
		link = eachone.replace('\n','')
		link_list.append(link)

start = time.time()
for eachone in link_list:
	# print(eachone)
	try:
		r = requests.get(eachone)
		print(r.status_code,eachone)
	except Exception as e:
		print("ERROR",e)
# r = requests.get('http://www.baidu.com')
# print(r.status_code)

end = time.time()
print("Total time is :",end-start)











