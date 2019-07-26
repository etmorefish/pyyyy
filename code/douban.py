#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 12:01:31
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import requests
from bs4 import BeautifulSoup

movie_list = []
def get_html():
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'	,'Host': 'movie.douban.com'}
	
	for i in range(0,26):
		link = 'https://movie.douban.com/top250?start='+str(i*25)
		r = requests.get(link,headers = headers,timeout = 20)
		print(str(i+1),'页面的状态码为：',r.status_code)
		soup = BeautifulSoup(r.text,'lxml')
		div_list = soup.find_all('div',class_= 'hd')
		for it in div_list:
			movie = it.a.span.text.strip()
			movie_list.append(movie)

	return movie_list
movies = get_html()
# with open ("top250.txt","a+") as f:
# 	f.write(str(movie_list))
# 	f.close()
print(movie_list)
