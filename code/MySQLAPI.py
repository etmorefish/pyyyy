#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 13:03:48
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$

import MySQLdb

class MySQLAPI(object):
	"""docstring for MySQLAPI"""
	def __init__(self, db_ip, db_name, db_password, table_name, db_charset):
		# super(MySQLAPI, self).__init__()
		self.db_ip = db_ip
		self.db_name = db_name
		self.db_password = db_password
		self.db_charset = db_charset
		self.conn = MySQLAPI(host = self.db_ip, user = self.db_name, password = self.db_password, 
								db = self.table_name, charset = self.db_charset)
		self.cur = self.conn.cursor()
		sql = "INSERT INTO hupu(title,author,post_link,author_page,start_date,reply,view,last_reply,date_time)"












