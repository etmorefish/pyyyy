# -*- coding:utf-8 -*-
import requests
from lxml import html
from urllib.parse import urljoin
from datetime import datetime
from scrapy import Request
from .base import EpaperSpider
from ..items import PaperItem, PageItem, ArticleItem


class CanNewsSpider(EpaperSpider):
    name = '中国航空报'
    base_url = 'http://ep.cannews.com.cn/publish/zghkb7/'
    date_format = ''
    publish_date = datetime.now().strftime('%Y-%m-%d')

    def __init__(self, *args, **kwargs):
        r = requests.get(self.base_url)
        root = html.fromstring(r.text)
        content = root.xpath('string(//meta[@http-equiv="refresh"]/@content)')
        url = content.replace('1; url=', '')
        self.base_url = urljoin(self.base_url, url)

    def start_requests(self):
        yield Request(self.base_url, callback=self.parse)

    def parse(self, response):
        # 提取各个版面链接
        hrefs = response.xpath('//a[@id="pageLink"]/@href').extract()
        for index, href in enumerate(hrefs):
            if index == 0:
                yield Request(response.urljoin(href), callback=self.parse_page, meta= {'is_headlines': 1}, dont_filter=True)
            else:
                yield Request(response.urljoin(href), callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        # 提取版面信息
        banner = response.xpath('//div[@class="l_t"]/text()').extract_first('').strip()
        number, name = self.split_banner(banner, '')
        image = response.urljoin(response.xpath('//img[@usemap="#PagePicMap"]/@src').extract_first(''))
        pdf_url = ''
        article_hrefs = [response.urljoin(url) for url in response.xpath('//div[@id="titleList"]/ul/li/a/@href').extract()]
        periodical = response.xpath('//div[@id="riqi_"]/text()').extract_first('').strip('&nbsp')

        # 首页版面
        if response.meta.get('is_headlines') == 1:
            paper = PaperItem()
            paper['periodical'] = periodical
            paper['origin_image'] = image
            paper['layout_name'] = name
            paper['layout_number'] = number
            paper['url'] = response.url
            paper['pdf_url'] = pdf_url
            yield paper

        # 版面
        page = PageItem()
        page['layout_number'] = number
        page['layout_name'] = name
        page['origin_image'] = image
        page['pdf_url'] = pdf_url
        page['url'] = response.url
        page['periodical'] = periodical
        page['article_counts'] = len(article_hrefs)
        page['article_number'] = ', '.join([str(i) for i in range(1, len(article_hrefs) + 1)])
        yield page

        # 热区坐标
        self.set_coords(response)

        # 文章连接
        for index, url in enumerate(article_hrefs):
            response.meta['article_number'] = index + 1
            response.meta['layout_name'] = name
            response.meta['layout_number'] = number
            yield Request(url, callback=self.parse_article, meta=response.meta)

    def parse_article(self, response):
        # 提取文章信息
        article = ArticleItem()
        article['title'] = response.xpath('//h1[@id="title2"]//text()').extract_first('').strip()
        article['leadtitle'] = response.xpath('//h2[@id="title1"]//text()').extract_first('').strip()
        article['subtitle'] = response.xpath('//h3[@id="title1"]//text()').extract_first('').strip()
        article['url'] = response.url
        article['content'] = u'\n'.join(response.xpath('//div[@id="wenzhang"]//p[not(@align)]/text()').extract()).strip()
        article['coords'] = self.coords[response.url.replace('/node', '//node')]
        image_links = response.xpath('//div[@id="wenzhang"]//img/@src').extract()
        article['origin_image_list'] = [response.urljoin(url) for url in image_links]
        article['article_number'] = response.meta.get('article_number', '')
        article['layout_number'] = response.meta.get('layout_number', '')
        article['layout_name'] = response.meta.get('layout_name', '')
        article['publish_date'] = response.meta.get('article_number', '')
        article['is_headlines'] = response.meta.get('is_headlines', 0)
        article['author'] = ''
        article['reporter'] = ''
        article['keywords'] = ''
        article['source'] = ''
        article['is_original'] = 1
        yield article
