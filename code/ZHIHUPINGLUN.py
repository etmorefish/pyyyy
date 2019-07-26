#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 15:11:46
# @Author  : lilei (849078367@qq.com)
# @Link    : https://zhuanlan.zhihu.com/p/31127887
# @Version : $Id$

"""
import requests
import json
# 第二页地址 https://api-zero.livere.com/v1/comments/list?callback=jQuery1124011494707799324821_1547107059053&limit=10&offset=2&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1547107059060
link = "https://api-zero.livere.com/v1/comments/list?callback=jQuery11240156339877647788_1547105603421&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1547105603423"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
r = requests.get(link,headers = headers)
# 获取 json 的 string
json_string = r.text
json_string = json_string[json_string.find('{'):-2]

json_data = json.loads(json_string)
print(json_data)
comment_list = json_data['results']['parents']

for eachone in comment_list:
    message = eachone['content']
    print (message)

"""


import requests
import json

def single_page_comment(link):

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
    r = requests.get(link, headers= headers)
    # 获取 json 的 string
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
	    message = eachone['content'] 
	    print (message)


for page in range(1,4):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963316"
    page_str = str(page)
    link = link1 + page_str + link2



    print (link)
    single_page_comment(link)

    



