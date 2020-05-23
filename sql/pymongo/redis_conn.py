# -*- coding: utf-8 -*-
# @Time    : 20-2-18 下午8:16
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : redis_conn.py
# @Software: PyCharm

import redis


# 建立连接
# conn = redis.StrictRedis(db=2, decode_responses=True)
# conn = redis.StrictRedis(db=2, decode_responses=True)


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
# res = conn.hgetall('hk')
# print(res)

# # 增
# conn.rpush('k', 'v1', 'v2')
# conn.lpush('k', 'v3', 'v4')
#
# # 查
# res = conn.lrange('k', 0, 10)
# print(res)
# res1 = conn.lindex('k', 1)
# # 改
# conn.lset('k', 1, 'v')
#
# # 删
# res = conn.lpop('k')
# print(res)
# res = conn.rpop('k')

class MyRedisList:
    def __init__(self, db=0, decode_responses=False):
        self.conn = redis.StrictRedis(db=db, decode_responses=decode_responses)

    def push(self, key, *values, direction='r'):
        if direction == 'r':
            self.conn.rpush(key, *values)
        else:
            self.conn.lpush(key, *values)

    def search(self, key, start, end=None):
        if end:
            return self.conn.lrange(key, start, end)

        else:
            return self.conn.lindex(key, start)


if __name__ == '__main__':
    r = MyRedisList(db=1, decode_responses=True)
    # r.push('k', 'hahah', 'leilei', direction='r')
    print(r.search('k', 0, 10))