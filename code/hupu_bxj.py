#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-13 17:06:48
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import requests
from bs4 import BeautifulSoup
import datetime 
import time 

# 获取页面内容 此网站使用gzip封装，需要使用r.content进行解封装  由utf-8解码为unicode
def get_page(link):	
	# link = 'https://bbs.hupu.com/bxj'
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	r = requests.get(link,headers = headers)
	html = r.content
	html = html.decode('UTF-8')
	soup = BeautifulSoup(html,"lxml")
	return soup

#对返回的HTML信息进行处理的到虎扑步行街list信息
def get_data(post_list):
	data_list = []
	for post in post_list:
		title = post.find('div',class_="titlelink box").a.text.strip()
		post_link =  post.find('div',class_="titlelink box").a['href']
		post_link = 'https://bbs.hupu.com'+post_link
		author_div = post.find('div',class_="author box")
		author = author_div.find('a',class_="aulink").text.strip()
		author_page = author_div.find('a',class_="aulink")['href']
		start_data = author_div.select('a:nth-of-type(2)')[0].get_text()
		reply_view = post.find('span',class_='ansour box').text.strip()
		reply = reply_view.split('/')[0].strip()
		view = reply_view.split('/')[1].strip()
		reply_div = post.find('div',class_="endreply box")
		reply_time = reply_div.a.text.strip()
		last_reply = reply_div.find('span',class_='endauthor').text.strip()
		date_time = str(datetime.date.today())+' '+ reply_time

     
		# if ':' in reply_time:
		# 	date_time = str(datetime.date.today())+' '+ reply_time
		# 	date_time = datetime.datetime.strptime(date_time,'%Y-%m-%d %H:%M')
		# else:
		# 	date_time = datetime.datetime.strptime(reply_time,'%Y-%m-%d').date()

		data_list.append([title,author,post_link,author_page,start_data,reply,view,last_reply,date_time])
	return data_list
for i in range(1,10):
	link = 'https://bbs.hupu.com/bxj-'+str(i)
	print('开始第%s页数据爬取...' %i)
	soup = get_page(link)
	soup = soup.find('div',class_='show-list')
	post_list = soup.find_all('li')
	data_list = get_data(post_list)
	# for each in data_list:
	# 	print(each)
	with open('hupu_bxj.txt','w') as f:
		for each in data_list:
			f.write(str(each))
		
			

	print('第%s页爬取完成！' %i)
	time.sleep(5)











