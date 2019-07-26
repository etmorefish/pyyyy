import os

template = """
# -*- coding:utf-8 -*-
from scrapy import Request
from .base import EpaperSpider
from ..items import PaperItem, PageItem, ArticleItem


class {spider_class}Spider(EpaperSpider):
    name = '{spider_name}'
    base_url = '{base_url}'
    date_format = '{date_format}'

    def parse(self, response):
        # 提取各个版面链接
        hrefs = response.xpath('{paper_hrefs_xpath}').extract()
        for index, href in enumerate(hrefs):
            if index == 0:
                yield Request(response.urljoin(href), callback=self.parse_page, meta= {{'is_headlines': 1}}, dont_filter=True)
            else:
                yield Request(response.urljoin(href), callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        # 提取版面信息
        banner = response.xpath('{banner_xpath}').extract_first('').strip()
        number, name = self.split_banner(banner, '')
        image = response.urljoin(response.xpath('{image_xpath}').extract_first(''))
        pdf_url = response.urljoin(response.xpath('{pdf_xpath}').extract_first('')) if '{pdf_xpath}' else ''
        article_hrefs = [response.urljoin(url) for url in response.xpath('{article_xpath}').extract()]
        periodical = response.xpath('{periodical_xpath}').extract_first('').strip() if '{periodical_xpath}' else ''

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
        article['title'] = response.xpath('{title_xpath}').extract_first('').strip()
        article['leadtitle'] = response.xpath('{leadtitle_xpath}').extract_first('').strip() if '{leadtitle_xpath}' else ''
        article['subtitle'] = response.xpath('{subtitle_xpath}').extract_first('').strip() if '{subtitle_xpath}' else ''
        article['url'] = response.url
        content = response.xpath('{content_xpath}').extract()
        content = [i.strip() for i in content if i.strip()]
        article['content'] = u'\\n'.join(content)
        article['coords'] = self.coords[response.url]
        image_links = response.xpath('{image_links_xpath}').extract()
        article['origin_image_list'] = [response.urljoin(url) for url in image_links]
        images_desc_el = response.xpath('{images_desc_xpath}') if '{images_desc_xpath}' else ''
        article['images_desc'] = [i.xpath('string(.)').extract_first('').strip() for i in images_desc_el]

        article['article_number'] = response.meta.get('article_number', '')
        article['layout_number'] = response.meta.get('layout_number', '')
        article['layout_name'] = response.meta.get('layout_name', '')
        article['publish_date'] = response.meta.get('article_number', '')
        article['is_headlines'] = response.meta.get('is_headlines', 0)
        article['author'] = response.xpath('{author_xpath}').extract_first('').strip() if '{author_xpath}' else ''
        article['reporter'] = response.xpath('{reporter_xpath}').extract_first('').strip() if '{reporter_xpath}' else ''
        article['keywords'] = response.xpath('{keywords_xpath}').extract_first('').strip() if '{keywords_xpath}' else ''
        article['source'] = response.xpath('{source_xpath}').extract_first('').strip() if '{source_xpath}' else ''
        is_original = response.xpath('{is_original_xpath}').extract_first('') if '{is_original_xpath}' else ''
        article['is_original'] = 0 if is_original else 1
        yield article
"""

if __name__ == "__main__":
    from seed.cannews import data, file_name
    result = template.format(**data)
    path = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(path, "newspapers", "spiders", file_name)
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'w') as f:
        f.write(result)
