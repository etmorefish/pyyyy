# -*- coding: utf-8 -*-
# @Time    : 19-7-26 上午11:16
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : dedaoapp.py
# @Software: PyCharm

from mitmproxy import ctx

def response(flow):
    print(flow.request.url)
    print(flow.response.text)
