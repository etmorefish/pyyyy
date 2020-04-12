# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NongnetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 供求关系
    supply = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 发布时间
    create_time = scrapy.Field()
    # 发布单位
    unit = scrapy.Field()
    # 联系人
    contact = scrapy.Field()
    # 手机号码
    phone = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 上市时间
    market_time = scrapy.Field()
