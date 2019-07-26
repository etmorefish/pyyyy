# -*- coding:utf-8 -*-
# @Author: wmy
# @Time: 2019/4/10 10:57
# @Description:

import math
import time

import redis
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.commands import ScrapyCommand
from scrapy.utils.conf import arglist_to_dict
from scrapy.exceptions import UsageError
from scrapy.utils.project import get_project_settings
from ..connection import get_redis_db
from datetime import date, timedelta, datetime

# CRAWL_DAYS = 0为爬取今天的数据 ，1 爬取隔一天的数据，以上则递增
CRAWL_DAYS = 0
# 抓取过往数据的开关
CRAWL_OLD_SWITCH = False


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)

    def get_option(self, option, opts, default):
        cmd_option = opts.spargs.get(option)
        setting_option = get_project_settings().get(option.upper())
        if cmd_option:
            return cmd_option
        elif setting_option:
            return setting_option
        else:
            return default

    # def run(self, args, opts):
    #     """插入redis队列"""
    #     redis_db = get_redis_db()
    #     spider_loader = self.crawler_process.spider_loader
    #     sps = spider_loader.list()
    #     redis_db.lpush('newspaper_spiders', *sps)

    def run(self, args, opts):
        """循环读取redis，判断根据取出的数量判断"""
        redis_db = get_redis_db()
        # configure_logging()
        # runner = CrawlerRunner()
        while True:
            crawl_list = []
            # TODO 常量改到settings里
            for i in range(2):
                spider = redis_db.lpop('newspaper_spiders')
                if spider:
                    crawl_list.append(spider)
                else:
                    break
            if crawl_list != []:
                for spidername in crawl_list:
                    # runner.crawl(spidername, **opts.spargs)
                    self.crawler_process.crawl(spidername, **opts.spargs)
                    print('此时启动的爬虫为：%s' % spidername)
                # d = runner.join()
                # d.addBoth(lambda _: reactor.stop())
                # reactor.run()  # the script will block here until all crawling jobs are finished
                self.crawler_process.start()
            if 0 < len(crawl_list) < 50:
                # 一轮爬取结束
                time.sleep(1800)
            if len(crawl_list) == 0:
                time.sleep(60)






# def get_redis_db():
#     REDIS_DATABASE = {
#         'host': '127.0.0.1',
#         'port': 6379,
#         # 'password': '123qweasdzxc',
#         'db': 0,
#     }
#     pool = redis.BlockingConnectionPool(
#         host=REDIS_DATABASE['host'],
#         port=REDIS_DATABASE['port'],
#         db=REDIS_DATABASE['db'],
#         # password=REDIS_DATABASE['password'],
#         decode_responses='utf-8',
#         max_connections=3
#     )
#     return redis.StrictRedis(connection_pool=pool)
