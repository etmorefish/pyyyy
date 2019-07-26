# -*- coding:utf-8 -*-
import re
from scrapy import Request
from .base import EpaperSpider
from datetime import datetime
from ..items import PaperItem, PageItem, ArticleItem


class FarmerSpider(EpaperSpider):
    name = '农民日报'
    base_url = 'http://szb.farmer.com.cn/{}001.html'
    date_format = '%Y/%Y%m%d/%Y%m%d_001/%Y%m%d_'

    def __init__(self, *args, **kwargs):
        self.publish_date = kwargs.get('publish_date', datetime.today().date())
        self.start_urls = [self.base_url.format(self.publish_date.strftime(self.date_format))]


    def parse(self, response):
        # 提取各个版面链接
        num = ''.join(re.compile('banciArray="(.+?)"').findall(response.text)).split(',')
        base = self.start_urls[0]
        hrefs = [re.sub('_\d{3}', f"_{i}", base) for i in num]
        for index, href in enumerate(hrefs):
            if index == 0:
                yield Request(response.urljoin(href), callback=self.parse_page, meta= {'is_headlines': 1}, dont_filter=True)
            else:
                yield Request(response.urljoin(href), callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        # 提取版面信息
        banner = ''.join(response.xpath('//span[@id="curbanci"]/..//text()').extract())
        number, name = self.split_banner(banner, '')
        image = response.urljoin(response.xpath('//img[@id="imageth"]/@src').extract_first(''))
        pdf_url = response.xpath('//a[contains(@onclick, ".pdf")]/@onclick').extract_first('')
        pdf_url = re.findall("href='(.+?)'", pdf_url)[0]
        pdf_url = response.urljoin(pdf_url)

        article_hrefs = response.xpath('//tr[contains(@class, "items")]/@onclick').extract()
        article_hrefs = [re.findall("href='(.+?)'", i)[0] for i in article_hrefs]
        article_hrefs = [response.urljoin(i) for i in article_hrefs]
        periodical = ''

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
        article['title'] = response.xpath('//td[@class="font01"]/text()').extract_first('').strip()
        article['leadtitle'] = ''
        article['subtitle'] = ''
        article['url'] = response.url
        content = response.xpath('//td[@class="font6"]//p/text()').extract()
        content = [i.strip() for i in content if i.strip()]
        article['content'] = u'\n'.join(content)
        article['coords'] = self.coords[response.url]
        image_links = response.xpath('//td[@class="font6"]//img/@src').extract()
        article['origin_image_list'] = [response.urljoin(url) for url in image_links]
        # images_desc_el = response.xpath('') if '' else ''
        # article['images_desc'] = [i.xpath('string(.)').extract_first('').strip() for i in images_desc_el]

        article['article_number'] = response.meta.get('article_number', '')
        article['layout_number'] = response.meta.get('layout_number', '')
        article['layout_name'] = response.meta.get('layout_name', '')
        article['publish_date'] = response.meta.get('article_number', '')
        article['is_headlines'] = response.meta.get('is_headlines', 0)
        author = response.xpath('//td[@class="font02"]/text()').extract()
        if author:
            author = author[-1].strip()
            if len(author) <= 3:
                article['author'] = author
        article['reporter'] = response.xpath('').extract_first('').strip() if '' else ''
        article['keywords'] = response.xpath('').extract_first('').strip() if '' else ''
        article['source'] = response.xpath('').extract_first('').strip() if '' else ''
        is_original = response.xpath('').extract_first('') if '' else ''
        article['is_original'] = 0 if is_original else 1
        yield article
