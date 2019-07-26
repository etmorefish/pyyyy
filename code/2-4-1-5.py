#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 21:12:29
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$
import operator

dicts = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorteds = sorted(dicts.items(),key=operator.itemgetter(1))

print(sorteds)