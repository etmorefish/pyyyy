#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 11:22:42
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import requests
key_dict = {'key1':'value1','key2':'value2'}
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# r = requests.get('http://httpbin.org/get',params = key_dict,headers=headers)
r = requests.post('http://httpbin.org/post',data = key_dict)
print(r.url)
print(r.text)
