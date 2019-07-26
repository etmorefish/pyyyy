# -*- coding: utf-8 -*-
# @Time    : 19-6-25 下午2:25
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : baidu.py
# @Software: PyCharm
import re

import  execjs
import requests
import  json
def get_sign(word):
    ctx = execjs.compile(open('baidu.js').read())
    res = ctx.call('e', word)
    return res

url = 'https://fanyi.baidu.com/v2transapi'
session = requests.session()
session.headers.update( {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'})
index = session.get('https://fanyi.baidu.com')
index = session.get('https://fanyi.baidu.com')
index.encoding='utf-8'

token = re.findall(r"token: '(.*?)'",index.text)[0]
gtk = re.findall(r"window.gtk = '(.*?)'",index.text)[0]
# print(gtk,token)

word = input('INPUT:')
form_date={
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': get_sign(word),
    'token': token

}

res = session.post('https://fanyi.baidu.com/v2transapi',data=form_date).json()
print(res.get('trans_result').get('data')[0].get('dst'))
# for k,v in res.json().items():
#     print(k,v)