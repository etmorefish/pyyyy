# -*- coding: utf-8 -*-
import scrapy


class ExampleSpiderSpider(scrapy.Spider):
    name = 'example_spider'
    # allowed_domains = ['dddd']
    start_urls = ['http://example.webscraping.com/places/default/user/login']

    def parse(self, response):
        formkey = response.xpath('//input[@name="_formkey"]/@value').extract_first()

        if formkey:
            data = {
                'email': '1213@qq.com',
                'password': '123456',
                '_next': '/places/default/index',
                '_formkey': formkey,
                '_formname': 'login',
            }
            yield scrapy.FormRequest(url='http://example.webscraping.com/places/default/user/login',
                                     formdata=data,
                                     callback=self.login_after)

        else:
            print('登录失败')

    def login_after(self, response):
        username = response.xpath('//a[@class="dropdown-toggle"]/text()').extract_first()

        if username:
            print('登录成功：当前用户{}'.format(username))
        else:
            print('error')