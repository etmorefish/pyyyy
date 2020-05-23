# -*- coding: utf-8 -*-
# @Time    : 20-2-27 下午9:47
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : house.py
# @Software: PyCharm

import pymongo

# 建立连接
client = pymongo.MongoClient()

# 指定数据库
db = client['house']
# 指定集合
house = db['lianjia_House']
village = db['lianjia_village']


res1 = house.find_one()
print(res1)
print(res1['_id'])

res2 = village.find()
print(res2.count())  # 2639
# res = house.find()
# n = 0
# for i in res:
#     n += 1
# print(n)   #59076

# 查
# res = my_col.find_one()
# print(res)

# res = my_col.find()
# print(res)  # <pymongo.cursor.Cursor object at 0x7f52181120f0>
# for i in res:
#     print(i)

# 改
# my_col.update_one({'name':'qiao'}, {'$set': {'age': 20}})
# res = my_col.find_one({'name':'qiao'})
# print(res)