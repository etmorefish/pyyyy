# -*- coding: utf-8 -*-
# @Time    : 20-5-22 下午5:40
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : logging_rt.py
# @Software: PyCharm


# import logging
# from datetime import datetime
# # 配置
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="时间: %(asctime)s 文件名: %(filename)s 行号: %(lineno)d",
#     filename='my.log',
#     filemode='a'
# )
#
# now = datetime.now()
# print(now)
#
# # 级别又低到高
# logging.debug(now)
# logging.info(now)  # 空白
# logging.warning(now)  #WARNING:root:2020-05-22 17:44:04.963432
# logging.error(now)
# logging.critical(now)

'''
INFO:root:2020-05-22 17:50:53.640258
WARNING:root:2020-05-22 17:50:53.640258
ERROR:root:2020-05-22 17:50:53.640258
CRITICAL:root:2020-05-22 17:50:53.640258
'''
'''
时间: 2020-05-22 17:54:36,042 文件名: logging_rt.py 行号: 22
时间: 2020-05-22 17:54:36,042 文件名: logging_rt.py 行号: 23
时间: 2020-05-22 17:54:36,043 文件名: logging_rt.py 行号: 24
时间: 2020-05-22 17:54:36,043 文件名: logging_rt.py 行号: 25
'''

# ------------------------------
# logging 模块化组件使用
# 创建一个logger对象
# 定义handler,决定吧日志发到哪里
#         StreamHandler --> 输出到控制台
#         FileHandler  --> 输出到文件
# 设置日志级别和输出格式Formatters
# 把handler]添加到对应的logger中去
# -------------------------------
import logging

my_logger = logging.Logger('bai')  # 创建一个日志处理器对象

# 第一个处理器
mh  = logging.FileHandler('bai.log')  # 定义一个handler
mh.setLevel(logging.INFO)   # 设置日志级别
fmt = logging.Formatter('时间: %(asctime)s  %(message)s 行号: %(lineno)d')
# 添加
mh.setFormatter(fmt)
my_logger.addHandler(mh)

# 第二个处理器
yh = logging.StreamHandler()
yh.setLevel(logging.DEBUG)
fmt1 = logging.Formatter('时间: %(asctime)s  %(message)s 行号: %(lineno)d --StreamHandler')

yh.setFormatter(fmt1)
my_logger.addHandler(yh)

# 设置完添加后,使用
my_logger.info('我是日志组件')