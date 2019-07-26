#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime    : 2018/9/1 下午3:38
# @Author      : Cheng Cheng
# @Description :
import redis
import pymysql
from twisted.enterprise import adbapi

MYSQL_DATABASE = {
    'host': 'localhost',
    'port': 3306,
    'database': 'bj_cj_data',
    'password': 'admin',
    'user': 'root',
}

# MYSQL_DATABASE = {
#     'host': '172.16.40.2',
#     'port': 3306,
#     'database': 'test',
#     'password': 'XWCJ_crawl@2',
#     'user': 'xwcj',
# }
REDIS_DATABASE = {
    'host': 'localhost',
    'port': 6379,
    # 'password': '123qweasdzxc',
    'db': 0,
}

# REDIS_DATABASE = {
#     'host': '172.16.40.2',
#     'port': 6379,
#     # 'password': '123qweasdzxc',
#     'db': 0,
# }

def get_redis_db():
    pool = redis.BlockingConnectionPool(
        host=REDIS_DATABASE['host'],
        port=REDIS_DATABASE['port'],
        db=REDIS_DATABASE['db'],
        # password=REDIS_DATABASE['password'],
        decode_responses='utf-8',
        max_connections=3
    )
    return redis.StrictRedis(connection_pool=pool)

redis_db = get_redis_db()

dbparams = dict(
        host=MYSQL_DATABASE['host'],
        db=MYSQL_DATABASE['database'],
        user=MYSQL_DATABASE['user'],
        passwd=MYSQL_DATABASE['password'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        use_unicode=True,
)
def get_pymysql_connect():
    conn = pymysql.connect(**dbparams)
    return conn

def get_dbpool():
    return adbapi.ConnectionPool('pymysql', **dbparams)


