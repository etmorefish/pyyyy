import scrapy
from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # return {
        #     'name': response.css('title::text').extract_first(),
        #     'url': response.url,
        # }
        urls = response.xpath('//a/@href').extract()
        for url in urls:
            yield scrapy.Request(url)

        title = response.xpath('//title/text()').extract_first()
        if title:
            yield {'url':response.url,'title':title}



'''
步骤
修改原来的父类 继承RedisSpider
修改settings里面的配置
启动之前 往redis—key 里面添加url就可以
'''
