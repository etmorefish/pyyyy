# -*- coding: utf-8 -*-
# @Time    : 20-5-21 下午11:40
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : demo.py
# @Software: PyCharm


import pymysql

# 1.建立连接
# pymysql.connect(
#     user='root',
#     password='sixqwe123',
#     db='spiders',
#     charset='utf-8',
# )
db_config = {
    "user": 'root',
    "password": 'sixqwe123',
    "db": 'spiders',
    "charset": 'utf8',
}
conn = pymysql.connect(**db_config)

# 2.获取游标
cur = conn.cursor()

# 3.执行sql语句
# res = cur.execute("select * from student")
# print(res)
cur.execute("select * from td")
# print(cur.fetchone())
# print(cur.fetchall())
# print(cur.fetchmany(4))
row = cur.fetchone()
while row:
    print("row: ", row)
    row = cur.fetchone()

# python操作MySQL默认使用事物模式,可以预防风险
# 插入时需要加上conn.commit()  rollback()

# 上下文管理
# with conn.cursor() as cur:
#     cur.execute("insert into td value(10, 'qqq', 21, 'M', 5)")
# conn.commit()


# 4.关闭游标
cur.close()

# 5.关闭连接
conn.close()