# -*- coding: utf-8 -*-
# @Time    : 20-2-3 下午1:41
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : fy.py
# @Software: PyCharm
import json
import re
import requests
from lxml import etree

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

resp = requests.get(url)
resp.encoding = 'utf-8'
# resp = resp.content.decode('utf-8')
html = etree.HTML(resp.text)
# rest = etree.tostring(html)
data = html.xpath('//script[@id="getAreaStat"]/text()')
title = html.xpath('//title/text()')
# print(html)
# print(rest.decode('utf-8'))
# print(title)
# print(data[0])

s = re.findall('window.getAreaStat = \[(.*?)\]\}catch\(e\)',data[0])[0]

res = eval(s)
res = eval(s)
nmg = res[26]
# print(res, type(res), len(res))
# print(nmg, type(nmg))
provinceName = nmg['provinceName']
confirmedCounts = nmg['confirmedCount']
deadCounts = nmg['deadCount']
curedCounts = nmg['curedCount']
print('provinceName ',provinceName, '  confirmedCount ',confirmedCounts,' deadCount ',deadCounts, ' curedCount ',curedCounts )
cities = nmg['cities']

# for i in cities:
#     print(i)
    # for k,v in i.items():
    #     print(k,v)

confirmedCount = []
deadCount = []
curedCount = []
for i in cities:
    confirmedCount.append(i.get('confirmedCount'))
    deadCount.append(i.get('deadCount'))
    curedCount.append(i.get('curedCount'))

print(confirmedCount)
print(deadCount)
print(curedCount)