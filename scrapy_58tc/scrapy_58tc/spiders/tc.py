import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['sh.58.com/sou/?key=python开发']
    start_urls = ['https://sh.58.com/sou/?key=python开发/']

    def parse(self, response):
        span = response.xpath("//div[@id='filter']/div[@class='tabs']/a/span")[0]
        
        print(span.extract())