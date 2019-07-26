# -*- coding: utf-8 -*-
import scrapy


class TencentSpidersSpider(scrapy.Spider):
    name = 'tencent_spiders'
    allowed_domains = ['ddddddd']
    start_urls = ['http://ddddddd/']

    def parse(self, response):
        pass
