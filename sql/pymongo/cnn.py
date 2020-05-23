# -*- coding: utf-8 -*-
# @Time    : 20-2-18 下午3:50
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : cnn.py
# @Software: PyCharm

import pymongo

# 建立连接
client = pymongo.MongoClient()

# 指定数据库
db = client['python']

# 指定集合
my_col = db['student']

# 增删改查
# 增
# my_col.insert_one({'name': 'lei', 'age': 20, 'sex':"M"})

# my_col.insert_many([
#     {'name': 'zhang', 'age': 19, 'sex': "F"},
#     {'name': 'jian', 'age': 18, 'sex': "F"},
#     {'name': 'qiao', 'age': 18, 'sex': "M"},
# ])

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

# 删
res = my_col.delete_one({'name':'qiao'})
print(res)    # <pymongo.results.DeleteResult object at 0x7f368c2be988>