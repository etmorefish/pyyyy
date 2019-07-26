#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 20:56:32
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


class Person():
	name = []

P1 = Person()
P2 = Person()
P1.name.append(1)
print(P1.name)
print(P2.name)
print(Person.name)