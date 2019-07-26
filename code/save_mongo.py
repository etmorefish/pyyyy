#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-12 21:24:40
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $I

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime

client = MongoClient('localhost',27017)
db = client.blog_database
collection = db.blog

link = 'http://www.santostang.com/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link,headers = headers)

soup = BeautifulSoup(r.text,"lxml")
title_list = soup.find_all('h1',class_="post-title")
for eachone in title_list:
	url = eachone.a['href']
	title = eachone.a.text.strip()
	post = { "url":url,
			"title": title,
			"date": datetime.datetime.utcnow()
			}
	collection.insert_one(post)
"""
#退出root用户
exit
#重启服务
sudo service mongod restart
https://www.cnblogs.com/weschen/p/7395667.html
关闭／启动
　　sudo service mongodb stop 　　sudo service mongodb start
show collections


"""
