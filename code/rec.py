#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 20:00:57
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$



import re  
# m = re.match("www","www.santostang.com")
# print(m)
# print(m.span())
# print(m.start())
# print(m.end())

# line  = "Fat cats a b c d  are smarter than a b c dogs, is it right?"
# m = re.match(r'(.*) a (.*?) dogs',line)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.groups())

# m = re.match("com","www.santostang.com")
# print(m)
# m = re.search("com","www.santostang.com")
# print(m)

m_match = re.match('[0-9]+','12345 is the first number, 23456 is the second')
m_search = re.search('[0-9]+','12345 is the first number, 23456 is the second')
m_findall = re.findall('[0-9]+','12345 is the first number, 23456 is the second')
print(m_match.group())
print(m_search.group())
print(m_findall)




