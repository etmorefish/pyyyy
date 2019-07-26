# -*- coding: utf-8 -*-
# @Time    : 19-7-24 下午5:04
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : count_http.py
# @Software: PyCharm


from mitmproxy import ctx

def request(flow):
    flow.request.headers['myheader'] = 'value'

class Counter:
    def __init__(self):
        self.num = 0

    def request(self,flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows"% self.num)

addons = [
    Counter()
]