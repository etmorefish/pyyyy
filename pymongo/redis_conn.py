# -*- coding: utf-8 -*-
# @Time    : 20-2-18 下午8:16
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : redis_conn.py
# @Software: PyCharm

import redis

# 建立连接
# conn = redis.StrictRedis(db=2, decode_responses=True)
conn = redis.StrictRedis(db=2, decode_responses=True)


# 使用redis命令
# string
# conn.set('k', 'v')
# conn.set('name', '雷蕾')
# res = conn.get('name')
# print(res)
# print(res.decode('utf-8'))

# key操作
# res = conn.keys('*')
# print(res)
# res = conn.delete('a')
#
# print(res)   # 0:不存在 1:原本存在
# res = conn.rename('name', 'new_name')
# print(res)
# res = conn.expire('new_name', 100)   # 设置过期时间
# print(conn.ttl('new_name'))
# conn.persist('new_name')  # 删除过期时间

# hash
# conn.hset('hk', 'f', 'v')
# conn.hmset('hk', {'name': 'fei', 'age': 18})
res = conn.hgetall('hk')
print(res)