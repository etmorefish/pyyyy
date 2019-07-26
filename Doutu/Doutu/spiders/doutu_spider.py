# -*- coding: utf-8 -*-
import scrapy
from ..items import DoutuItem

class DoutuSpiderSpider(scrapy.Spider):
    name = 'doutu_spider'
    # allowed_domains = ['ddddd']
    start_urls = ['http://www.doutula.com/']

    def parse(self, response):
        image_urls = response.xpath('//a[@class="col-xs-6 col-sm-3"]/img/@data-original').extract()
        items = DoutuItem()

        if image_urls:
            items['image_urls'] = image_urls
            yield items
