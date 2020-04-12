# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import NongnetItem
from scrapy_redis.spiders import RedisSpider


class NongnetSpiderSpider(RedisSpider):
    name = 'nongnet_spider'
    # allowed_domains = ['dddd']
    # start_urls = ['http://www.nongnet.com/']
    redis_key = 'nongnet:start_urls'

    base_url = 'http://www.nongnet.com'

    def parse(self, response):
        '''
        匹配详情页以及下一页的
        :param response:
        :return:
        '''
        detail_urls = response.xpath('//li[@class="lileft"]//a/@href').extract()

        for detail_url in detail_urls:
            yield scrapy.Request(url=self.base_url+detail_url, callback=self.parse_detail)

        next_url = response.xpath('//span[@id="ContentMain_lblPage"]/a/@href').extract()[-2]
        if next_url:
            yield scrapy.Request(url=self.base_url+next_url, callback=self.parse)

    def parse_detail(self, response):
        items = NongnetItem()

        title_result = response.xpath('//h1/text()').extract_first()
        if title_result:
            items['supply'] = title_result.strip()[1:2]
            items['title'] = title_result.strip()[3:]

        create_time = response.xpath('//font[@color="999999"]/text()').re('\d+/\d+/\d+ \d+:\d+')
        if create_time:
            items['create_time'] = create_time[0]

        unit = re.findall(r"发布单位</div><div class='xinxisxr'><a href='.*?'>(.*?)</a>", response.text, re.S)
        if unit:
            items['unit'] = unit[0]
        else:
            items['unit'] = ''

        address = re.findall(r"所在地区</div><div class='xinxisxr'><a href='.*?' title='.*?' >(.*?)</a> <a href='.*?'  title='.*?'>(.*?)</a> <a href='.*?'>(.*?)</a>",response.text, re.S)
        if address:
            items['address'] = '-'.join(address[0])


        contact = re.findall(r"联 系 人</div><div class='xinxisxr'>(.*?)</div>", response.text, re.S)
        if contact:
            items['contact'] = contact[0]

        phone = re.findall(r"手机号码</div><div class='xinxisxr'>(.*?)</div>", response.text, re.S)
        if phone:
            items['phone'] = phone[0]

        market_time = re.findall(r"上市时间</div><div class='xinxisxr'>(.*?)</div>", response.text, re.S)
        if market_time:
            items['market_time'] = market_time[0]


        yield items