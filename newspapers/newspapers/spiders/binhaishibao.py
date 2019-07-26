# -*- coding:utf-8 -*-
# @Author: wmy
# @Time: 19-3-12 上午10:34
# @Description:

from urllib.parse import urljoin
from scrapy import Request, Spider
from datetime import datetime

from .base import EpaperSpider
from ..items import PaperItem, PageItem, ArticleItem


class BHSBSpider(Spider):
    name = '滨海时报'

    base_url = 'http://bhsb.tjbh.com/html/{}/node_1.htm'
    date_format = '%Y-%m/%d'
    coords = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.publish_date = kwargs.get('publish_date', datetime.today().date())
        self.start_urls = [self.base_url.format(self.publish_date.strftime(self.date_format))]

    def parse_start_url(self, response):
        ################ start ###################
        # pdf 或者banner 可能只在版面页里
        ################# end ####################
        hrefs = response.xpath('//table[@width="380"]//tr/td/a[@id="pageLink"]/@href').extract()
        for index, href in enumerate(hrefs):
            if index == 0:
                yield Request(response.urljoin(href), callback=self.parse_page,
                              meta={'is_headlines': True}, dont_filter=True)
            else:
                yield Request(response.urljoin(href), callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        page = PageItem()
        banner = response.xpath('string(//td[@width="145" and @align="left"])').extract_first('').strip()
        ################ start ###################
        # banner 的提取，有时只再parse_start_url的response
        number, name = banner.split('：')
        ################# end ####################
        page['layout_number'] = number.strip()
        page['layout_name'] = name.strip()

        page['origin_image'] = response.urljoin(response.xpath('//img[@usemap="#PagePicMap"]/@src').extract_first())
        page['pdf_url'] = response.urljoin(
            response.xpath('//td[@width="50" and @align="right"]/a/@href').extract_first(''))
        page['url'] = response.url

        ################ start ###################
        # 新增字段
        page['paper_name'] = self.name
        page['periodical'] = ''

        # todo 考虑area区有重复的文章链接，需要先进行处理

        page['article_counts'] = len(response.xpath('//area'))

        # 文章在版面图的顺序位置， 需要传递给下一级解析, 提取的位置可能不能再冲area里提取
        # 感觉这里存个列表比较迷
        page['article_number'] = ', '.join(range(len(response.xpath('//area'))))
        ################# end ####################
        yield page

        ################ start ###################
        # 首页的文章需要做标记
        if response.meta.get('is_headlines'):
            paper = PaperItem()
            paper['paper_name'] = self.name
            paper['periodical'] = ''
            paper['origin_image'] = page['origin_image']
            paper['layout_name'] = name.strip()
            paper['layout_number'] = number.strip()
            paper['url'] = response.url
            paper['pdf_url'] = page['pdf_url']
            paper['layout_number'] = number.strip()
            yield paper
        ################# end ####################

        hrefs = []
        for area in response.xpath('//area'):
            article_url = area.xpath('./@href').extract_first('')

            ################ start ###################
            # 提取coords 方法更合理的写在基类里
            # 由于新增的版次顺序号，感觉问斩article 和 coords 分开还是好点
            coords = area.xpath('@coords').extract_first().strip()
            self.coords[urljoin(response.url, article_url)] = coords
            ################# end ####################
            hrefs.append(urljoin(response.url, article_url))

        for index, url in enumerate(hrefs):

            ################ start ###################
            # 1. 文章的链接可能有多余的后缀 url.endswith('-1')，
            # 2. 也有一种可能是文章是同一个url导致无法插入到mysql中

            # 烦人的的版次顺序号
            response.meta['article_number'] = index
            response.meta['layout_name'] = page['layout_name']
            response.meta['layout_number'] = page['layout_number']
            yield Request(url, callback=self.parse_article, meta=response.meta)
            ################# end ####################

    def parse_article(self, response):
        article = ArticleItem()
        title_el = response.xpath('//td[@class="font01"]')
        article['title'] = title_el.xpath('string(.)').extract_first('').strip()
        article['leadtitle'] = ''.join(
            title_el.xpath('string(../preceding-sibling::tr[1]/td[@class="font02"])').extract()).strip()
        article['subtitle'] = ''.join(
            title_el.xpath('string(../following-sibling::tr[1]/td[@class="font02"])').extract()).strip()
        article['url'] = response.url

        ################ start ###################
        # 删除字段
        # article['referer'] = response.request.headers['Referer'].decode('utf-8')
        ################# end ####################

        article['content'] = u'\n'.join(response.xpath('//div[@id="ozoom"]//p//text()').extract()).strip()
        article['coords'] = self.coords[response.url]
        image_links = response.xpath('//*[@id="newspic"]//img/@src').extract()
        article['origin_image_list'] = [response.urljoin(url) for url in image_links]
        images_desc_el = response.xpath('//*[@id="newspic"]//img/../../following-sibling::tr[1]/td')
        article['images_desc'] = [i.xpath('string(.)').extract_first('').strip() for i in images_desc_el]

        ################ start ###################
        # 新增字段

        # 可以在基类 或是 管道 加
        article['paper'] = self.name
        article['publish_date'] = self.publish_date

        # 通过meta传值的新加字段
        article['article_number'] = response.meta.get('article_number', '')
        article['layout_number'] = response.meta.get('layout_number', '')
        article['layout_name'] = response.meta.get('layout_name', '')
        article['publish_date'] = response.meta.get('article_number', '')

        # 新加提取字段
        article['author'] = response.xpath('').extract_first('').strip()
        article['reporter'] = response.xpath('').extract_first('').strip()
        article['keywords'] = response.xpath('').extract_first('').strip()
        article['source'] = response.xpath('').extract_first('').strip()
        is_original = response.xpath('').extract_first('').strip()
        article['is_original'] = 1 if is_original else 0
        ################# end ####################
        yield article
