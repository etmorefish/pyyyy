# -*- coding: utf-8 -*-
# @Time    : 20-5-22 下午6:23
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : sha.py
# @Software: PyCharm


import hashlib

# 二进制
# res = hashlib.new('md5', '毛雷'.encode())
res = hashlib.md5('金属'.encode())
print(res.digest())
print(res.hexdigest()) # fbcb34191ca8b610fae10ce440bcb85d

# update
res1 = hashlib.sha256()
res1.update('金属'.encode())
print(res1.hexdigest())
res1.update('行号'.encode())
print(res1.hexdigest())

with open('my.log','r') as f:
    data = f.read()
    res1.update(data.encode())
    print(res1.hexdigest())  # 95f93b5e58fd511a5a3585192bf3796ae748dffb1c63e529fd0a638fa447aac0
