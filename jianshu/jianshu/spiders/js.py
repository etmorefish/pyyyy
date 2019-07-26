# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow='p/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # 获取内容页数据并解析数据
        title=response.xpath("//h1[@class='title']/text()").get()
        #作者图像
        avatar=response.xpath("//a[@class='avatar']/img/@src").get()
        author=response.xpath("//span[@class='name']/a/text()").get()
        #发布时间
        pub_time=response.xpath("//span[@class='publish-time']/text()").get()
        #详情页id
        url=response.url
        url1=url.split("?")[0]
        article_id=url1.split("/")[-1]
        #文章内容
        content=response.xpath("string(//div[@class='show-content'])").extract()
        content = [i.strip().replace('\n','').replace('\xa0','') for i in content if i.strip()]


        item = JianshuItem(
            title=title,
            avatar=avatar,
            author=author,
            pub_time=pub_time,
            origin_url=response.url,
            article_id=article_id,
            content=content
        )

        return item
