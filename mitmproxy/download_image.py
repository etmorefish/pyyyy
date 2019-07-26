# -*- coding: utf-8 -*-
# @Time    : 19-7-24 下午5:29
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : download_image.py
# @Software: PyCharm
import os
from mitmproxy import ctx

base_dir = os.path.dirname(os.path.abspath(__file__))

class DownloadImage:

    def load(self,loader):
        # 添加一个开启模式
        loader.add_option(
            name='image_download',
            typespec = bool,
            default = False,
            help = '下载访问到的所有图片'
        )
        #增加一个图片大小过滤
        loader.add_option(
            name='image_minisize',
            typespec=int,
            default=1024,
            help='下载图片的最小单位/bytes'
        )
        loader.add_option(
            name='image_dir',
            typespec=str,
            default='',
            help='图片存放路径'
        )

    def response(self,flow):
        min_size = ctx.options.image_minisize
        content_type = flow.response.headers.get('content-type')
        if not content_type:
            return

        if 'image' not in content_type:
            return

        if int(flow.response.headers['Content-Length']) >= min_size:
            host = flow.request.host
            image_dir = ctx.options.image_dir
            if image_dir:
                if not os.path.exists(image_dir):
                    os.mkdir(image_dir)
            else:
                image_dir = base_dir

            if not os.path.exists(os.path.join(image_dir,host)):
                os.mkdir(os.path.join(image_dir,host))

            image_name = flow.request.path.split('?')[0].split('/')[-1]
            image_path = os.path.join(image_dir,host,image_name)
            with open(image_path,'wb') as f:
                f.write(flow.response.content)
            ctx.log.info("Successfully downloading images: %s from %s"%(image_name,flow.request.http_version+host+flow.request.path))


        



addons = [
    DownloadImage()
]