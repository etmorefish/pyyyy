# -*- coding: utf-8 -*-

import re
import os
import hashlib
from datetime import datetime

from scrapy.http import Request
from scrapy.utils.python import to_bytes
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

from newspapers.connection import get_dbpool
from newspapers.items import PaperItem, PageItem, ArticleItem

settings = get_project_settings()


class SaveImagePipeline(ImagesPipeline):
    """保存图片"""

    def get_media_requests(self, item, spider):
        if item.get('origin_image_list'):
            return [Request(x, meta={'name': spider.spider.name}) for x in item['origin_image_list']]
        if item.get('origin_image'):
            return Request(item['origin_image'], meta={'name': spider.spider.name})

    def item_completed(self, results, item, spider):
        local_image_list = []
        for index, rs in enumerate(results):
            local_image_list.append('')
            if rs[0]:
                if item.get('origin_image'):
                    item['local_image'] = rs[1]['path']
                if item.get('origin_image_list'):
                    local_image_list[index] = rs[1]['path']
                    item['local_image_list'] = local_image_list
        return item

    def file_path(self, request, response=None, info=None):
        """定义文件路径"""
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest() + '.jpg'
        return os.path.join(info.spider.publish_date.strftime('%Y-%m'),
                            info.spider.publish_date.strftime('%Y%m%d'),
                            request.meta['name'],
                            image_guid)


class HandleDataPipeline(object):
    """数据清洗管道"""

    def process_item(self, item, spider):
        # 清洗，处理数据
        for k, v in item.items():
            if isinstance(v, str):
                item[k] = v.strip()
            elif isinstance(v, list):
                item[k] = ', '.join(v)
            elif v is None:
                item[k] = ''

        # 统一赋值
        item['paper_name'] = spider.name
        item['publish_date'] = spider.publish_date
        item['fetch_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 根据类别单独处理
        if isinstance(item, PageItem):
            item['layout_number'] = self.handler_page_number(item.get('layout_number', ''), item.get('layout_name', ''))
        elif isinstance(item, ArticleItem):
            if not item['is_headlines']:
                item['is_headlines'] = 0
            if not item['is_original']:
                item['is_original'] = 1
        return item

    def handler_page_number(self, number, name):
        """处理版次值"""
        if number == '当前版':
            num = re.findall(r'(\d+)', name)
        else:
            num = re.findall(r'(\d+)', number)
        number_letter = re.findall(r'([a-zA-Z]+)', number)
        if num and num[0]:
            new_number = '{:02d}'.format(int(num[0]))
            if number_letter and number_letter[0]:
                new_number = number_letter[0] + new_number
            return new_number


class SaveDataPipeline(object):
    """保存数据到数据库"""

    def __init__(self):
        self.dbpool = get_dbpool()
        self.fetch_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.save_item, item)
        return item

    def save_item(self, cur, item):
        if isinstance(item, PaperItem):
            table = 'digital_paper'
        elif isinstance(item, PageItem):
            table = 'digital_paper_layout'
        else:
            table = 'digital_paper_article'
        try:
            key_list = list(item.keys())
            sql = 'insert into {table} (`{key}`) values ({value}) on DUPLICATE key update {update}'.format(
                table=table,
                key='`, `'.join(key_list),
                value=', '.join(['%s'] * len(key_list)),
                update=', '.join(['`{}`=%s'.format(i) for i in key_list])
            )
            value = [item.get(key, '') for key in key_list] * 2
            cur.execute(sql, value)
        except Exception as e:
            print(e)
