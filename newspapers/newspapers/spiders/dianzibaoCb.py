# -*- coding:utf-8 -*-
from scrapy import Request
from .base import EpaperSpider
from ..items import PaperItem, PageItem, ArticleItem


class dianzibaoCbSpider(EpaperSpider):
    name = '中国经营报'
    base_url = 'http://dianzibao.cb.com.cn/html/{}/node_1.htm'
    date_format = '%Y-%m/%d'

    def parse(self, response):
        # 提取各个版面链接
        hrefs = response.xpath('//td[@class="default"]/a[@id="pageLink"]/@href').extract()
        for index, href in enumerate(hrefs):
            if index == 0:
                yield Request(response.urljoin(href), callback=self.parse_page, meta= {'is_headlines': 1}, dont_filter=True)
            else:
                yield Request(response.urljoin(href), callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        # 提取版面信息
        banner = response.xpath('//td[@class="default"]/a[@id="pageLink"]/text()').extract_first('').strip()
        number, name = self.split_banner(banner, '')
        image = response.urljoin(response.xpath('//map[@name="PagePicMap"]/../img/@src').extract_first(''))
        pdf_url = response.urljoin(response.xpath('//td[@class="default"]/../td[2]/a/@href').extract_first('')) if '//td[@class="default"]/../td[2]/a/@href' else ''
        article_hrefs = [response.urljoin(url) for url in response.xpath('//map[@name="PagePicMap"]/area/@href').extract()]
        periodical = response.xpath('').extract_first('').strip() if '' else ''

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
        article['leadtitle'] = response.xpath('//td[@class="font02"][0]/text()').extract_first('').strip() if '//td[@class="font02"][0]/text()' else ''
        article['subtitle'] = response.xpath('//td[@class="font02"][1]/text()').extract_first('').strip() if '//td[@class="font02"][1]/text()' else ''
        article['url'] = response.url
        article['content'] = u'\n'.join(response.xpath('//div[@id="ozoom"]//p/text()').extract()).strip()
        article['coords'] = self.coords[response.url]
        image_links = response.xpath('//td[@class="font6"]/../..//img/@src').extract()
        article['origin_image_list'] = [response.urljoin(url) for url in image_links]
        images_desc_el = response.xpath('//td[@class="font6"]/../..//img/../../../tr[2]//p/text()') if '//td[@class="font6"]/../..//img/../../../tr[2]//p/text()' else ''
        article['images_desc'] = [i.xpath('string(.)').extract_first('').strip() for i in images_desc_el]

        article['article_number'] = response.meta.get('article_number', '')
        article['layout_number'] = response.meta.get('layout_number', '')
        article['layout_name'] = response.meta.get('layout_name', '')
        article['publish_date'] = response.meta.get('article_number', '')
        article['is_headlines'] = response.meta.get('is_headlines', 0)
        article['author'] = response.xpath('').extract_first('').strip() if '' else ''
        article['reporter'] = response.xpath('').extract_first('').strip() if '' else ''
        article['keywords'] = response.xpath('').extract_first('').strip() if '' else ''
        article['source'] = response.xpath('').extract_first('').strip() if '' else ''
        is_original = response.xpath('').extract_first('') if '' else ''
        article['is_original'] = 0 if is_original else 1
        yield article
