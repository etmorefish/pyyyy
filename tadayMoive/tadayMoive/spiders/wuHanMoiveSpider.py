# -*- coding: utf-8 -*-
import scrapy

from tadayMoive.items import TadaymoiveItem


class WuhanmoivespiderSpider(scrapy.Spider):
    name = 'wuHanMoiveSpider'
    # allowed_domains = ['dddddd']
    start_urls = ['http://www.jycinema.com/html/default/index.html']

    def parse(self, response):
        sub = response.xpath('//div[@id="hotfilmlist"]')
        items = []
        for s in sub:

            item = TadaymoiveItem()
            item['moiveName'] = s.xpath('.//div[@class="film-list"]/a/span/text()').extract()
            items.append(item)
        return items