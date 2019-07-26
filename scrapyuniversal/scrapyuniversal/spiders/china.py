# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ScrapyuniversalItem


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow='article/\d+/.*?.html'),  callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]')),
    )

    def parse_item(self, response):
        item = ScrapyuniversalItem()

        item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        item['url'] = response.url
        item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
        item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)').strip()
        item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源：(.*)').strip()
        item['website'] = '中华网'

        yield  item
'''
https://tech.china.com/article/20190627/kejiyuan0129317460.html
https://tech.china.com/article/20190625/kejiyuan0129316295.html
https://tech.china.com/article/\d+/.*?.html
<a href="http://tech.china.com/articles/index_2.html" class="a1">下一页</a>
2018-03-25 13:31:30
item['title'],item['url'],item['text'],item['datetime'],item['source'],item['website']
'''

