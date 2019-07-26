# -*- coding: utf-8 -*-
# @Time    : 19-7-16 下午2:49
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : zhihu_hot.py
# @Software: PyCharm

import  requests

from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link').text()
    answer = pq(item.find('.content').html()).text()

    # file = open('explore.txt','a',encoding='utf-8')
    # file.write('\n'.join([question,author,answer]))
    # file.write('\n'+'='*50+'\n')
    # file.close()

    with open('explore.txt','w',encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')