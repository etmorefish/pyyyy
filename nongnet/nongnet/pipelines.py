# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from openpyxl import Workbook


class NongnetPipeline(object):

    wb = Workbook()  #实例
    ws = wb.active  #激活工作区
    ws.append(['供求关系','标题', '发布时间', '联系人', '手机号码', '地址', '上市时间', '发布单位'])

    def process_item(self, item, spider):
        try:
            line = [item['supply'], item['title'], item['create_time'], item['contact'],item['phone'],item['address'],item['market_time'],item['unit'] ]
        except Exception as e:
            return item
        else:
            self.ws.append(line)
            self.wb.save('nongnet.xlsx')
            return item



class MongoPipeline(object):

    # def __init__(self, MONGODB_HOST='127.0.0.1', MONGODB_PORT=27017):
    #     client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    #     db = client['nong']
    #     self.connection = db['items']
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     print('ok -------------------')
    #     return cls(MONGODB_HOST=crawler.settings['MONGODB_HOST'], MONGODB_PORT=crawler.settings['MONGODB_PORT'])
    # #
    def open_spider(self,spider):
        client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        db = client['nongnet']
        self.connection = db['items']

    def process_item(self, item, spider):
        try:
            self.connection.insert(dict(item))
            print(item,'ok---------')
            # self.connection.save(item)
        except:
            print('数据存储异常.....')

        return item