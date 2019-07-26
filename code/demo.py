# !/usr/bin/env python
# -*- coding:utf-8 -*-
# create_time: 2019/6/24
# Author = '心蓝'


import requests
from lxml import etree

response = requests.get('http://spxy.cau.edu.cn/col/col22476/index.html')
response.encoding = 'utf-8'
page = etree.HTML(response.text)
urls = page.xpath('//div[@class="teacher"]/a/@href')

for url in urls:
    url = 'http://spxy.cau.edu.cn' + url
    res = requests.get(url)
    res.encoding = 'utf-8'
    per_page = etree.HTML(res.text)
    info = per_page.xpath('//div[@class="info-main"]/p//text()')
    title = per_page.xpath('//div[@class="info-main"]/p/strong//text()')
    data = {}
    temp = []
    for item in title:
        temp.append(info.index(item))

    for i in range(len(temp)):
        if i == 0 and temp[i] != 0:
            data['个人介绍'] = '\r\n'.join(info[:temp[i]])

        if i == len(temp) - 1:

            data[info[temp[i]]] = '\r\n'.join(info[temp[i]+1:])

        else:

            data[info[temp[i]]] = ('\r\n'.join(info[temp[i]+1:temp[i+1]])).replace('\xa0', '')

    print(data)
    # exit()