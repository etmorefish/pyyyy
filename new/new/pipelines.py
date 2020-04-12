# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class NewPipeline(object):

    def open_spider(self,spider):
        client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        connection = client['new_1633']
        self.db = connection['item']

    def process_item(self, item, spider):
        try:
            self.db.save(item)
        except:
            print('数据存储异常.....')

        return item
