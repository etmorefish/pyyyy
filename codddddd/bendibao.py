# -*- coding: utf-8 -*-
# @Time    : 20-4-29 下午6:00
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : bendibao.py
# @Software: PyCharm

import re
import requests
import datetime
from lxml import etree
from pandas import DataFrame

url_bdb = 'http://m.bendibao.com/news/xiaofeiquan/city.php'
url = 'http://m.hz.bendibao.com/news/xiaofeiquan/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

# 提取所有的url
res_a = requests.get(url=url_bdb, headers=headers)
html_bdb = res_a.content.decode('UTF-8')
a = etree.HTML(html_bdb)
item_urls = a.xpath("//div[@class='col-xs-4 col-sm-3 col-md-2 col-lg-1']/a/@href")

n = 0
shengs = []
shis = []
methors = []
times = []
moneys = []
totals = []

for i in item_urls:

    # 详细页面
    print(n , i)
    res = requests.get(url = i, headers = headers)
    html = res.content.decode('UTF-8')
    r = etree.HTML(html)


    sheng = r.xpath('//div[@class="select"]/select[1]/option[@selected]/text()')[0]
    shi = r.xpath('//div[@class="select"]/select[2]/option[@selected]/text()')[0]

    data = r.xpath('//div[@class="list-detail"]')[0]
    methor = data.xpath('//div[1]/span[2]/text()')[0]
    time = data.xpath('//div[2]/span[2]/text()')[0]
    # time = re.findall('年(.*)日', time)[0]
    # s_time = re.split('-|至',time)[0].replace('日','').replace('月','-')
    # over_time = re.split('-|至',time)[1]
    # if '月' in over_time:
    #     o_time = over_time.replace('月','-')
    # else:
    #     o_time = s_time.split('-')[0] + '-' + over_time
    # print(s_time, o_time, type(s_time))

    # d1 = datetime.datetime(2020, int(s_time.split('-')[0]), int(s_time.split('-')[1]))
    # d2 = datetime.datetime(2020, int(o_time.split('-')[0]), int(o_time.split('-')[1]))
    # totals_day = (d2 - d1).days

    money = data.xpath('//div[3]/span[2]/text()')
    if money[0]:
        money = money[0]
    total = data.xpath('//div[4]/span[2]/text()')
    if total == []:
        total = '未知'
    else:
        total = total[0]
    n = n+1
    shengs.append(sheng)
    shis.append(shi)
    methors.append(methor)
    times.append(time)
    moneys.append(money)
    totals.append(total)


    # print(total)
data = {
    '省份': shengs,
    '城市': shis,
    '领取方式': methors,
    '发放时间': times,
    '发放金额': moneys,
    '领取数量': totals

}
df = DataFrame(data)
df.to_csv('bendibao.csv',  index=False, header=True)