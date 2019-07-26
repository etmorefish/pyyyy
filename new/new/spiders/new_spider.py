# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NewSpiderSpider(CrawlSpider):
    name = 'new_spider'
    # allowed_domains = ['dddd']
    start_urls = ['https://www.163.com/']

    rules = (
        Rule(LinkExtractor(allow='http.*?://.*?.163.com/\d{2}/\d{4}/\d+/.*?.html'), callback='parse_item', follow=True),
    )
    # follow=False 只匹配当前页面

    def parse_item(self, response):
        i = {}
        i['artile_title'] = response.xpath('//h1/text()').extract_first()
        time = response.xpath('//div[@class="post_time_source"]/text()').re('\d+-\d+-\d+ \d+:\d+:\d+')
        if time:
            i['time'] = time[0]
        # i['content'] = response.xpath('//div[@class="post_text"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield i
