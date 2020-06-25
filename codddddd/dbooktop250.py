import requests
from lxml import etree
import re
import random
import json
from pandas import DataFrame

dbookname = []
dquote = []
drating_nums = []
dimgurl = []
dinfo = []
dauthor = []
dtranslater = []
dpublisher = []
ddate = []
dprice = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
}
for i in range(10):
    print('正在爬取第{}页'.format(i+1))
    url = 'https://book.douban.com/top250?start={}'.format(i*25)
    # url = 'https://book.douban.com/top250?start=0'

    resp = requests.get(url=url, headers=headers, timeout=10)
    # print("响应状态码:", resp.status_code)
    # if 200 != resp.status_code:
    #     return 404
    html = etree.HTML(resp.text)
    html = html.xpath('//tr[@class="item"]')
    bookname = html.xpath('//div[@class="pl2"]/a/@title')               #书名
    quote = html.xpath("//p[@class='quote']/span[@class='inq']/text()") #简介
    rating_nums = html.xpath('//span[@class="rating_nums"]/text()')     #评分
    rating_people_ = html.xpath('//span[@class="pl"]/text()')           #评价人数(未格式化)
    rating_people = []                                                  #评价人数(格式化)
    for i in rating_people_:
        e = re.findall('\d+',i)
        rating_people.append(e)
    imgurl = html.xpath('//a[@class="nbg"]/img/@src')                   #封面链接
    info = html.xpath('//p[@class="pl"]/text()')                        #出版信息集
    author = []                                                         #作者
    translater = []                                                     #翻译（外文作品有此属性）
    publisher = []                                                      #出版社
    date = []                                                           #发行日期
    price = []                                                          #价格
    for i in info:
        data = i.split('/')
        author.append(data[0])
        translater.append(data[1] if len(data) == 5 else 'none')
        publisher.append(data[-3] if data[-3] else 'none')
        # date.append(data[-2] if data[-2] else 'none')
        price.append(data[-1] if data[-1] else 'none')

    dbookname.extend(bookname)
    dquote.extend(quote)
    drating_nums.extend(rating_nums)
    dimgurl.extend(imgurl)
    dinfo.extend(info)
    dauthor.extend(author)
    dtranslater.extend(translater)
    dpublisher.extend(publisher)
    # ddate.extend(data)
    dprice.extend(price)

# print(bookname, rating_nums, author)

booktop = {
    'bookname': dbookname,
    'quote':dquote,
    'rating_nums': drating_nums,
    'imgurl': dimgurl,
    'info': dinfo,
    'author': dauthor,
    'translater': dtranslater,
    'publisher':dpublisher,
    # 'date': ddate,
    'price': dprice,
}



df = DataFrame(booktop)
df.to_csv('booktop250.csv', index=False,  header=True)
print('OK!')