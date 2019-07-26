# -*- coding: utf-8 -*-
import scrapy


class WuhanspiderSpider(scrapy.Spider):
    name = 'wuHanSpider'
    allowed_domains = ['wuhan.tianqi.com']
    start_urls = ['http://wuhan.tianqi.com/']

    def parse(self, response):
        pass
