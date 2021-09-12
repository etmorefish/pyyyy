import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.00.00.00.00.html']
    
    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        
        # src = response.xpath("//ul[@id='component_59']/li//img/@src")
        # name = response.xpath("//ul[@id='component_59']/li//img/@alt")
        # price = response.xpath("//ul[@id='component_59']/img/@src")
        # link = response.xpath("//ul[@id='component_59']/li//p[@class='price']/span[1]/text()")
        
        li_list = response.xpath("//ul[@id='component_59']/li")
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()   # 图片懒加载 
            # 第一张图片的地址和其他图片的地址不一一样
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            link = li.xpath('.//a/@href').extract_first()
            
            # print(src, name, price, link)
            book = ScrapyDangdangItem(src=src, name=name, price=price, link=link)
            
            # 获取一个book 就交给 pipelines
            yield book
        
        if self.page < 100:
            self.page += 1
            url = self.base_url + str(self.page) + '-cp01.54.00.00.00.00.html'

            yield scrapy.Request(url=url, callback=self.parse)
