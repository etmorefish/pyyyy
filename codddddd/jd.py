# -*- coding: utf-8 -*-
# @Time    : 20-4-19 下午7:57
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : jd.py
# @Software: PyCharm


import requests
import re
import time
import json
import pandas as pd

content_list = []
for i in range(99):
    print('正在爬去第{}页'.format(i+1))
    try:
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=4311178&score=0&sortType=5&page={}&pageSize=50&isShadowSku=0&fold=1'.format(
            i)
        r = requests.get(url).text
        datas = re.findall('comments":(.*)\}', r)[0]
        content = re.findall('"content":"(.*?)"', datas)
        content_list.extend(content)
        time.sleep(3)
    except:
        print('本页爬取失败')
df = pd.DataFrame()
df['评论'] = content_list
df.to_excel('A400.xlsx')