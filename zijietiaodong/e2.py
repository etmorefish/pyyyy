# -*- coding: utf-8 -*-
# @Time    : 19-7-2 下午8:05
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : e2.py
# @Software: PyCharm

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
