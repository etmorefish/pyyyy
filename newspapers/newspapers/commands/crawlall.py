import math
from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerRunner
from scrapy.utils.conf import arglist_to_dict
from scrapy.exceptions import UsageError
from scrapy.utils.project import get_project_settings
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

    def run(self, args, opts):
        spider_loader = self.crawler_process.spider_loader

        # 分页
        sps = spider_loader.list()
        total, page = int(opts.spargs.get('total', 1)), int(opts.spargs.get('page', 1))
        page_count = math.floor(len(sps) / total)
        start_index = (page - 1) * page_count
        end_index = len(sps)

        if total != page:
            end_index = page * page_count

        crawl_days = self.get_option('crawl_days', opts, CRAWL_DAYS)
        crawl_old_switch = self.get_option('crawl_old_switch', opts, CRAWL_OLD_SWITCH)

        if crawl_old_switch:
            date_start = date.today() - timedelta(days=int(crawl_days))
            date_end = date.today()
            while date_start <= date_end:
                publish_date = date_start
                for spidername in args or sps[start_index:end_index]:
                    opts.spargs['publish_date'] = publish_date
                    self.crawler_process.crawl(spidername, **opts.spargs)
                    print('此时启动的爬虫为：{}, 时间为：{}'.format(spidername, date_start.strftime('%Y-%m-%d')))
                date_start += timedelta(days=1)
            self.crawler_process.start()
        else:
            today = date.today().strftime('%Y-%m-%d')
            publish_date = self.get_option('publish_date', opts, today)
            publish_date = datetime.strptime(publish_date, '%Y-%m-%d')
            for spidername in args or sps[start_index:end_index]:
                opts.spargs['publish_date'] = publish_date
                # self.crawler_process.crawl(spidername, **opts.spargs)
                print('此时启动的爬虫为：%s' % spidername)
            # self.crawler_process.start()



    # def run(self, args, opts):
    #     spider_loader = self.crawler_process.spider_loader
    #
    #     crawl_days = self.get_option('crawl_days', opts, CRAWL_DAYS)
    #     crawl_old_switch = self.get_option('crawl_old_switch', opts, CRAWL_OLD_SWITCH)
    #
    #     if crawl_old_switch:
    #         date_start = date.today() - timedelta(days=int(crawl_days))
    #         date_end = date.today()
    #         while date_start <= date_end:
    #             publish_date = date_start
    #             for spidername in args or spider_loader.list():
    #                 opts.spargs['publish_date'] = publish_date
    #                 self.crawler_process.crawl(spidername, **opts.spargs)
    #                 print('此时启动的爬虫为：{}, 时间为：{}'.format(spidername, date_start.strftime('%Y-%m-%d')))
    #
    #             date_start += timedelta(days=1)
    #         self.crawler_process.start()
    #     else:
    #         today = date.today().strftime('%Y-%m-%d')
    #         publish_date = self.get_option('publish_date', opts, today)
    #         publish_date = datetime.strptime(publish_date, '%Y-%m-%d')
    #         for spidername in args or spider_loader.list():
    #             opts.spargs['publish_date'] = publish_date
    #             self.crawler_process.crawl(spidername, **opts.spargs)
    #             print('此时启动的爬虫为：%s' % spidername)
    #         self.crawler_process.start()
