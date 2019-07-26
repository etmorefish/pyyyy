from urllib.parse import urljoin
from datetime import datetime
from scrapy.spiders.crawl import Spider
from ..items import PaperItem, PageItem, ArticleItem
import re


class EpaperSpider(Spider):
    coords = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.publish_date = kwargs.get('publish_date', datetime.today().date())
        self.start_urls = [self.base_url.format(self.publish_date.strftime(self.date_format))]

    def split_banner(self, banner, split_str=''):
        """
        :param banner: banner :str
        :param split_str: 分割字符串 : str
        :return:
        """
        number, name =  re.findall("\d+",banner)[0], ''
        if split_str:
            _, name = banner.split(split_str)
        else:
            try:
                _, name= banner.split('：')
            except:
                try:
                    try:
                        _ , name = banner.split(':')
                    except:
                        _ , name =  banner.split(")")
                except:
                    pass

        return number.strip(), name.strip()

    def set_coords(self, response):
        for area in response.xpath('//area'):
            href = area.xpath('@href').extract_first().strip()
            coords = area.xpath('@coords').extract_first().strip()
            self.coords[urljoin(response.url, href)] = coords

    def handles_author(self,author):
        author = re.sub('作者：|:',"",author).strip()
        return author

    def handles_source(self, source):
        source = re.sub('来源：|:',"",source).strip()
        return source

    # def parse_start_url(self, response):
    #     paper = PaperItem()
    #     paper['name'] = self.name
    #     paper['publish_date'] = self.publish_date.strftime('%Y-%m-%d')
    #     paper['url'] = response.url
    #     paper['image'] = self.page_image(response)
    #     yield paper
    #
    #     for r in self.parse_home_page(response):
    #         yield r
    #
    # def page_image(self, response):
    #     raise NotImplementedError
    #
    # def parse_home_page(self, response):
    #     self.set_coords(response)
