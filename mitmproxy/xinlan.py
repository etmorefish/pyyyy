# -*- coding: utf-8 -*-
# @Time    : 19-7-25 上午11:31
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : xinlan.py
# @Software: PyCharm


import os

from mitmproxy import ctx
base_dir = os.path.dirname(os.path.abspath(__file__))


class ImageDownload:

    def load(self, loader):
        loader.add_option(
            name='download_image',
            typespec=bool,
            default=False,
            help="Download the requested image"
        )

        loader.add_option(
            name='image_min_size',
            typespec=int,
            default=1024,
            help="Minimum size(bytes) of image to download"
        )

        loader.add_option(
            name='image_dir',
            typespec=str,
            default='',
            help='Image Storage Folder'
        )

    def response(self, flow):
        min_size = ctx.options.image_min_size
        if 'image' in flow.response.headers['content-type'] and int(flow.response.headers['Content-Length']) >= min_size:
            host = flow.request.host
            image_dir = ctx.options.image_dir
            if image_dir:
                if not os.path.exists(image_dir):
                    os.mkdir(image_dir)
            else:
                image_dir = base_dir

            if not os.path.exists(os.path.join(image_dir, host)):
                os.mkdir(os.path.join(image_dir, host))
            image_name = flow.request.path.split('?')[0].split('/')[-1]
            image_path = os.path.join(image_dir, host, image_name)
            with open(image_path, 'wb') as f:
                f.write(flow.response.content)
            ctx.log.info('Successfully downloading images: %s from %s' % (image_name, flow.request.http_version+host+flow.request.path))


addons = [
    ImageDownload()
]
