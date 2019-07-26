# -*- coding: utf-8 -*-
# @Time    : 19-6-23 下午3:26
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : test.py
# @Software: PyCharm

import json
str1 = "k:1|k1:2|k2:3|k3:4"
str1 = str1.replace('|', '","')
str1 = str1.replace(':', '":"')
str2 = '{"'+str1+'"}'
print (str2,type(str2))
print (json.loads(str2))


str1 = "k:1|k1:2|k2:3|k3:4"
def str2dict(str1):
    dict1 = {}
    for iterms in str1.split('|'):
        key,value = iterms.split(':')
        dict1[key] = value
    return dict1
print(str2dict(str1))
print('-'*100)
import json
dic = {'name': '张三'}
result = json.dumps(dic, ensure_ascii=False)
print(result)

from urllib import parse
str1 = "name=张三"
# 编码
str2 = parse.quote(str1)
print(str2)
# 解码
str3 = parse.unquote(str2)
print(str3)