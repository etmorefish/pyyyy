# -*- coding: utf-8 -*-
# @Time    : 19-7-16 下午4:00
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : quotes.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow='p/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # 获取内容页数据并解析数据



        item = JianshuItem(

        )

        return item

