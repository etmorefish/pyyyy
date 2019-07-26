# -*- coding: utf-8 -*-
# @Time    : 19-6-24 上午11:18
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : spxy_spider.py
# @Software: PyCharm

import requests
import re
import csv
from lxml import etree

url = 'http://spxy.cau.edu.cn/col/col22476/index.html'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
r = requests.get(url,headers=headers,timeout=20)
selector = etree.HTML(r.text)

teacher = selector.xpath('//div/a/@href')
# print(teacher)
urls = []
for i in teacher:
    if '/art' in i:
        urls.append('http://spxy.cau.edu.cn'+i)
# http://spxy.cau.edu.cn/art/2018/10/10/art_22476_590543.html
# http://spxy.cau.edu.cn/art/2019/3/26/art_22476_610697.html

fp = open('spxy.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('姓名','职称','电话','url','经历'))

for url in urls:
    res = requests.get(url, headers=headers, timeout=20)
    sel = etree.HTML(res.content.decode())
    name = sel.xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/h3/text()')
    job_title = sel.xpath('//*[@id="2-教授"]/text()')
    info = sel.xpath('string(//div[@class="info-main"])')
    tel = re.findall(r'话：(\d+-*\d+)',info)
    if len(tel[0])>6:
        print(tel[0])
    # email = re.compile(r'箱：(.*?)[z-a]$',info)
    writer.writerow((name[0], job_title[0], tel[0],url,info))
    print(tel[0])
    # print(info)
    print(url)
# print(name[0], job_title[0], tel[0],email[0],info)
fp.close()

# 单位 院系 姓名 职称 手机 电话 邮箱 研究方向/研究领域 学历经历 获奖或奖励 备注 网络来源 图片