# -*- coding: utf-8 -*-
# @Time    : 20-2-18 下午7:31
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : mysql_con.py
# @Software: PyCharm

# 开始  创建connection  获取cursor   执行查询、执行命令、获取数据、处理数据   关闭cursor  关闭connection  结束

import  pymysql

# 建立连接
db_config = {
    'user': 'root',
    'password': 'sixqwe123',
    'db': 'spiders',
    'charset': 'utf8',
}
conn = pymysql.connect(**db_config)
# 游标
cur = conn.cursor()

# 执行sql语句
# res = cur.execute("select * from student")
# print(res)

# cur.execute("select * from student")
# 避免内存爆
# row = cur.fetchone()
# while row:
#     print('row:', row)
#     row = cur.fetchone()

# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchall())
# print(cur.fetchmany(2))


# cur.execute("insert into student values(13, 'M', 18, 'jian',0)")
#
# conn.commit()
# cur.close()
# conn.close()
# 默认使用了事物模式


# 上下文管理
with conn.cursor() as cur:
    # cur.execute("insert into student values(14, 'M', 18, 'jia',0)")
    cur.execute("insert into student values(15, 'M', 18, 'jia',0)")
# conn.commit()
conn.rollback()