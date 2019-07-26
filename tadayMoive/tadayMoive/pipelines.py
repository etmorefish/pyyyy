# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class TadaymoivePipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d',time.localtime())
        fileName = 'wuHan'+now+'.txt'
        with open(fileName,'a') as f:
            f.write(item['moiveName'][0].encoding('utf-8')+'\n\n')
        return item
