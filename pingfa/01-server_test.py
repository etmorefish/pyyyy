#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 15:56:05
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$
'''写一个不断接受（while True）的服务端。他的作用是把客户端发来的数据原封不动返回。
'''
import socket

server = socket.socket() #shilihua
server.bind(('',8899))
server.listen(5)

while True:
	conn, addr = server.accept()
	while True:
		recv_data = conn.recv(1024)
		if recv_data:
			print(recv_data.decode())
			conn.send(recv_data)
		else:
			conn.close()
			break