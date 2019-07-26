#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 20:30:42
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$

import requests
import re 
from bs4 import BeautifulSoup
from lxml import etree
# 
# 1
link = 'http://www.santostang.com/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link,headers = headers)
html = r.text
# title_list = re.findall('<h1 class="post-title"><a href=".*?">(.*?)</a></h1>',html)
# print(title_list)

# 2
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())    #对代码进行美化
first_title = soup.find('h1',class_="post-title").a['href']
print("第一篇文章的标题是：",first_title)

title_list = soup.find_all('h1',class_="post-title")
for i in range(len(title_list)):
	title = title_list[i].a.text.strip()
	# print("第%s篇文章的标题是：%s"%((i+1),title))

h1 = soup.header.h1
# print(h1)

# for child in soup.header.div.descendants:
# 	print(child)

# aaa = soup.find_all(re.compile('<li><a href=".*?">(.*?)</a></li>'))
# aaa = soup.find_all(re.compile("^h"))
# for a in aaa:
# 	print(a.name)


# css选择器
# print(soup.select("header  h1"))
# print(soup.select("header  > h1"))
# print(soup.select("div > a"))

# print(len(soup.select("div > a")))
# for i in range(len(soup.select("div > a"))):
# 	print("-----%s--%s-------" % (i+1 ,soup.select("div > a")[i]))

# print(soup.select('a[href^="http://www.santostang.com/"]'))



# 3
htmls = etree.HTML(r.text)
title_list1 = htmls.xpath('//h1[@class="post-title"]/a/text()')
print(title_list1)






