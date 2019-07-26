# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpiderSpider(CrawlSpider):
    name = 'tencent_spider'
    # allowed_domains = ['ddddddd']
    start_urls = ['https://careers.tencent.com/search.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
