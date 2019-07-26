# -*- coding: utf-8 -*-
# @Time    : 19-7-16 下午3:25
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : save_mysql.py
# @Software: PyCharm


import  pymysql
db = pymysql.connect(host='localhost',user = 'root', password = 'sixqwe123' , port = 3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:',data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()