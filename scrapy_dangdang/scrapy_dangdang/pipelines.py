# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdangPipeline:
    
    def open_spider(self, spider):
        print('start spider ........')
        self.fp = open('book.json', 'w', encoding='utf-8')
    
    
    # item 就是 yeild 传过来的book对象
    def process_item(self, item, spider):
        # with open('book.json', 'a', encoding='utf-8') as f:
        #     f.write(str(item))
        
        self.fp.write(str(item))
            
        return item
    
    def close_spdier(self, spider):
        print('close spider ........')
        self.fp.close()
        
        
# 多条管道开启
import urllib.request

class DangDownloadPipeline:
    
    def process_item(self, item, spider):
        url = 'http:'+ item.get('src')
        filename = './books/'+item.get('name')+'.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        
        return item