# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperItem(scrapy.Item):
    paper_name = scrapy.Field()
    periodical = scrapy.Field()  # 刊期
    local_image = scrapy.Field()
    origin_image = scrapy.Field()
    layout_name = scrapy.Field()
    layout_number = scrapy.Field()
    url = scrapy.Field()
    pdf_url = scrapy.Field()
    fetch_date = scrapy.Field()
    publish_date = scrapy.Field()


class PageItem(scrapy.Item):
    paper_name = scrapy.Field()
    url = scrapy.Field()
    periodical = scrapy.Field()
    layout_name = scrapy.Field()
    layout_number = scrapy.Field()
    article_number = scrapy.Field()
    local_image = scrapy.Field()
    origin_image = scrapy.Field()
    pdf_url = scrapy.Field()
    article_counts = scrapy.Field()
    fetch_date = scrapy.Field()
    publish_date = scrapy.Field()


class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    publish_date = scrapy.Field()
    paper_name = scrapy.Field()
    article_number = scrapy.Field()
    layout_number = scrapy.Field()
    layout_name = scrapy.Field()
    title = scrapy.Field()
    leadtitle = scrapy.Field()
    subtitle = scrapy.Field()
    content = scrapy.Field()
    origin_image_list = scrapy.Field()
    local_image_list = scrapy.Field()
    images_desc = scrapy.Field()
    author = scrapy.Field()
    reporter = scrapy.Field()
    editor = scrapy.Field()
    coords = scrapy.Field()
    is_headlines = scrapy.Field()
    is_original = scrapy.Field()
    keywords = scrapy.Field()
    source = scrapy.Field()
    fetch_date = scrapy.Field()
