# -*- coding: utf-8 -*-
# @Time    : 20-5-24 下午2:10
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : jian.py
# @Software: PyCharm


import  requests

url = 'http://47.95.118.109:8870/DogeJian'

data = {
"data": "dogejian",
"num": 88218
}
res = requests.post(url, data)
print(res.text)