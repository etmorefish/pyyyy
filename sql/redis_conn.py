# -*- coding: utf-8 -*-
# @Time    : 20-5-22 上午12:31
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : demo.py
# @Software: PyCharm


import redis

# 1.建立连接
# conn  = redis.StrictRedis(db=0, decode_responses=True)
conn = redis.StrictRedis(db=1, decode_responses=True)

# 2.使用redis命令
# string
# conn.set('k', 'v')
# conn.set('name', '毛雷')
# res = conn.get('name')
# print(res)
# print(res.decode('utf-8'))

# 3.key操作, del-----> delete
# res = conn.keys('*')
# print(res)
# res = conn.delete('k')
# print(res)  # 0:不存在   1:存在
# res = conn.rename('name', 'new_name')
# print(res)  # True表示成功
# res = conn.expire('new_name', 100)  # 定时,设置过期时间
# print(res)
# print(conn.ttl('new_name'))   # 查看剩余过期时间
# conn.persist('new_name')     #   删除过期时间

# hash
# conn.hset('hk', 'f', 'v')
# conn.hmset('hk', {'name': 'lei', 'age': 21})
# print(conn.hgetall('hk'))
# print(conn.hvals('hk'))
# print(conn.hkeys('hk'))

# list rpush/lpush lrange/lindex lset/lpop/rpop
# conn.rpush('k', 'v1', 'v2')
# print(conn.lrange('k', 0, 10))
# conn.lpush('k', 'v3', 'v4')
print(conn.type('new_name'))