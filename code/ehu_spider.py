# -*- coding: utf-8 -*-
# @Time    : 19-6-24 上午9:38
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : ehu_spider.py
# @Software: PyCharm


# http://env.dhu.edu.cn/6959/list.htm
# 单位 院系 姓名 职称 手机 电话 邮箱 研究方向/研究领域 学历经历 获奖或奖励 备注 网络来源 图片
import requests
import re
import csv
from lxml import etree

url = 'http://env.dhu.edu.cn/6959/list.htm'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
r = requests.get(url,headers=headers,timeout=20)
selector = etree.HTML(r.content)
job = selector.xpath('//*[@id="container_content"]/table[2]/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td[2]/span/a/text()')[0]

urls = selector.xpath('//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]/a/@href')

# url = 'http://env.dhu.edu.cn/f1/1d/c8125a127261/page.htm'
fp = open('ehu.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('姓名','职称','电话','pic','邮箱','url','经历'))

for url in urls:
    res = requests.get(url, headers=headers, timeout=20)
    sel = etree.HTML(res.content)
    name = sel.xpath('//*[@id="infocontent"]/table/tbody/tr/td[2]/table[1]/tbody/tr[1]/td/div/div/text()')
    nam = name[0].replace('\r\n ', '')
    name = nam.replace(" ", "")
    pic = sel.xpath('//*[@id="infocontent"]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/span/span/div//img/@src')
    pic = 'http://env.dhu.edu.cn' + pic[0]
    info = sel.xpath('string(//div[@class="Article_Content"])')
    tel = re.findall(r'：(\d+-*\d+)', info)[-1]
    email = info.split('：')
    email = email[-1]
    writer.writerow((name, job, tel, pic, email,url, info))
    print(name, job, tel,pic, email,url, info)
fp.close()

# //*[@id="infocontent"]/table/tbody/tr/td[2]/table[1]/tbody/tr[1]/td/div/div/text()

'''
//*[@id="infocontent"]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/span/span/div/p[5]/img
//*[@id="infocontent"]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/span/span/div/p[2]/span/span/strong/img
//*[@id="infocontent"]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/span/span/div//img

# 单位 院系 姓名 职称 手机 电话 邮箱 研究方向/研究领域 学历经历 获奖或奖励 备注 网络来源 图片
//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]/span[1]/span/a/span
//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]/a[1]/span
//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]/a[2]/span
//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]/a[3]/span
//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]/a[4]/span
//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]/a[5]/span
//*[@id="container_content"]/table[2]/tbody/tr/td[4]/div/div[1]/div/p[3]

//*[@id="infocontent"]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/span/span/div/p[5]/img
//*[@id="infocontent"]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/span/span/div/p[2]/span[1]/span[1]/img
//*[@id="infocontent"]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/span/span/div/p[2]/span/span/strong/img

'''