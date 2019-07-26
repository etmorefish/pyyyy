# -*- coding:utf-8 -*-
# @Author: wmy
# @Time: 2019/3/4 14:04
# @Description:
import os
from scrapy.commands import crawl
from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError
from scrapy.utils.project import get_project_settings
from datetime import date, timedelta, datetime

# CRAWL_DAYS = 0为爬取今天的数据 ，1 爬取隔一天的数据，以上则递增
CRAWL_DAYS = 0
# 抓取过往数据的开关
CRAWL_OLD_SWITCH = False


class Command(crawl.Command):
    requires_project = True

    def syntax(self):
        return "[options] <spider>"

    def short_desc(self):
        return "Run a spider"

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")

    def get_option(self, option, opts, default):
        cmd_option = opts.spargs.get(option)
        setting_option = get_project_settings().get(option.upper())
        if cmd_option:
            return cmd_option
        elif setting_option:
            return setting_option
        else:
            return default

    def run(self, args, opts):

        if len(args) < 1:
            raise UsageError()
        elif len(args) > 1:
            raise UsageError("running 'scrapy crawl' with more than one spider is no longer supported")
        spname = args[0]

        crawl_days = self.get_option('crawl_days', opts, CRAWL_DAYS)
        crawl_old_switch = self.get_option('crawl_old_switch', opts, CRAWL_OLD_SWITCH)

        if crawl_old_switch:
            date_start = date.today() - timedelta(days=int(crawl_days))
            date_end = date.today()
            while date_start <= date_end:
                publish_date = date_start
                opts.spargs['publish_date'] = publish_date
                self.crawler_process.crawl(spname, **opts.spargs)
                date_start += timedelta(days=1)
            self.crawler_process.start()
        else:
            today = date.today().strftime('%Y-%m-%d')
            publish_date = self.get_option('publish_date', opts, today)
            publish_date = datetime.strptime(publish_date, '%Y-%m-%d')
            opts.spargs['publish_date'] = publish_date
            self.crawler_process.crawl(spname, **opts.spargs)
            self.crawler_process.start()
