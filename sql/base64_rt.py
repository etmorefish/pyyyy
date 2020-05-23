# -*- coding: utf-8 -*-
# @Time    : 20-5-22 下午6:18
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : base64_rt.py
# @Software: PyCharm


# 对称加密
# 非对称加密
# 单项加密
import  base64

data = '你好明天'

res = base64.b64encode(data.encode())
print(res)

data = 'hello world'

res = base64.b64encode(data.encode())
print(res)

data = 'hello worl'

res = base64.b64encode(data.encode())
print(res)
