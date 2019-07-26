# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

from twisted.enterprise import adbapi


class JianshuPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'sixqwe123',
            'database': 'scraping',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['origin_url'],item['article_id']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into jianshu(id,title,content,author,avatar,pub_time,origin_url,article_id) values(null,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql

    # def __init__(self):
    #     self.connect = pymysql.connect(
    #         host=settings.MYSQL_HOST,
    #         db=settings.MYSQL_DBNAME,
    #         user=settings.MYSQL_USER,
    #         passwd=settings.MYSQL_PASSWD,
    #         charset='utf8',
    #         use_unicode=True
    #     )
    #     self.cursor = self.connect.cursor();
    #
    # def process_item(self, item, spider):
    #     try:
    #         self.cursor.execute(
    #             "insert into article (body, author, createDate) value(%s, %s, %s) on duplicate key update author=(author)",
    #             (item['body'],
    #              item['author'],
    #              datetime.datetime.now()
    #              ))
    #         self.connect.commit()
    #     except Exception as error:
    #         logging.log(error)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.connect.close();