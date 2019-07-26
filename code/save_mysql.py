#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-12 18:59:28
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import MySQLdb
import requests
from bs4 import BeautifulSoup

conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'sixqwe123', db = 'scraping',charset = "utf8")
cur = conn.cursor()
# cur.execute("insert into urls (url,content) values('www.baidu.com','This is baidu')")

link = 'http://www.santostang.com/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link,headers = headers)

soup = BeautifulSoup(r.text,"lxml")
title_list = soup.find_all('h1',class_="post-title")
for eachone in title_list:
	url = eachone.a['href']
	title = eachone.a.text.strip()
	cur.execute("INSERT INTO urls (url, content) VALUES(%s, %s)",(url,title))

cur.close()
conn.commit()
conn.close()






