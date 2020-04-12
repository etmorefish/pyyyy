# -*- coding: utf-8 -*-
# @Time    : 20-4-11 下午11:42
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : www.py
# @Software: PyCharm

import re
import requests
from lxml import etree

# url = 'http://59.172.226.5:80/eams/sso/login.action?targetUrl={base64}aHR0cDovLzU5LjE3Mi4yMjYuNTo4MC9lYW1zL2hvbWUuYWN0aW9u'
# header = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
# headers = {'User-Agent': header}
# r = requests.get(url=url, headers = headers)
#
# lt = re.findall(r'name="lt" value="(.*)"',r.text)[0]
# print(r)
# # print(r.headers, r.text)
# print(lt)
def getxpath(html):
    return etree.HTML(html)

# 下面是我们实战的第一个html
sample1 = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""
# 获取xml结构
s1 = getxpath(sample1)

# 获取标题(两种方法都可以)
#有同学在评论区指出我这边相对路径和绝对路径有问题，我搜索了下
#发现定义如下图
print(s1.xpath('//title/text()'))
print(s1.xpath('/html/head/title/text()'))