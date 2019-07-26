#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 16:00:29
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$
# 写一个客户端来测试之前的服务端。
import socket

client = socket.socket()
client.connect(('127.0.0.1',8899))
sned_data = input('--->').encode()
client.send(sned_data)
recv_data = client.recv(1024)
print(recv_data.decode())





