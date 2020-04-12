# -*- coding: utf-8 -*-
# @Time    : 20-2-18 下午4:40
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : con.py
# @Software: PyCharm


import pymongo

# 建立连接
client = pymongo.MongoClient()

# 指定数据库
db = client['python']

# 指定集合
my_col = db['student']

class MyMongoDB:
    def __init__(self, database, collection):
        self.client = pymongo.MongoClient()
        self.db = self.client[database]
        self.collection = self.db[collection]

    def insert(self, data, onlyOne=True):
        if onlyOne:
            self.collection.insert_one(data)
        else:
            self.collection.insert_many(data)

if __name__ == '__main__':
    m = MyMongoDB('python', 'student')
    # 插入单条数据
    # my_data = {'name': 'fei', 'age': 21, 'sex': 'M'}
    # m.insert(my_data)
    #  插入多条数据
    my_data = [{'name': 'l12', 'age': 21, 'sex': 'F'}, {'name': 'q12a', 'age': 21, 'sex': 'F'}]
    m.insert(my_data, False)

    