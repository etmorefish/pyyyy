# -*- coding: utf-8 -*-
import  re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SohuSpiderSpider(CrawlSpider):
    name = 'sohu_spider'
    # allowed_domains = ['ddddd']
    start_urls = ['http://www.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow='http.*?://www.sohu.com/a/\d+_\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='/a/\d+_\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        url = response.url
        mpid = re.findall(r'http.*?://www.sohu.com/a/(\d+)_\d+',url)
        if mpid:
            yield scrapy.Request('http://v2.sohu.com/integration-api/mix/region/140?size=100&mpld={}'.format(mpid[0]),callback=self.parse_detail)
        #对数据解析

    def parse_detail(self,response):
        urls = re.findall(r'/a/\d+_\d+',response.text,re.S)
        # print(response.text)
        # print(urls)

        for url in urls:
            yield scrapy.Request('http://www.sohu.com/'+url,callback=self.parse_item)


        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
# http://www.sohu.com/a/325349604_405849?spm=smpc.home.top-news2.5.1562511619066iKOsfnK&_f=index_news_4
# http://www.sohu.com/a/325332472_428290?g=0?code=5c62bf75a348243f6a2ce993a01741fd&spm=smpc.home.top-news1.1.1562511619066iKOsfnK&_f=index_cpc_0
# http.*?://www.sohu.com/a/\d+_\d+
'''
scrapy shell http://www.sohu.com
>>> from scrapy.linkextractors import LinkExtractor
>>> art_url = LinkExtractor(allow="http.*?://www.sohu.com/a/\d+_\d+")
>>> art_url.extract_links
<bound method LxmlLinkExtractor.extract_links of <scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor object at 0x7fe5929b1208>>
>>> art_url.extract_links(response)
其他请求feider抓包
http://v2.sohu.com/integration-api/mix/region/140?size=100&mpld=298015267
'''