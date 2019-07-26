#!/usr/bin/python3
# coding: utf-8
import requests 
from bs4 import BeautifulSoup

url = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,'lxml')
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)
# print(r.text[:1000])?

with open('title.txt','a+') as f:
	f.write(title)
	f.close()
	


