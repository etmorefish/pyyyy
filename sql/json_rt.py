# -*- coding: utf-8 -*-
# @Time    : 20-5-22 下午4:53
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : json_rt.py
# @Software: PyCharm

import json

data = {
    'name': '李雷',
    'age': 18,
    'feature': ['找工作', '优秀', '厉害']
}

# dump/load
#
# with open('data', 'w') as f:
#     json.dump(data, fp=f, ensure_ascii=False)
#
# with open('data', 'r') as f:
#     res = json.load(fp=f)
#     print(res)

# dumps/loads
with open('data', 'w') as f:
    f.write(json.dumps(data, ensure_ascii=False))

with open('data', 'r') as f:
    res = json.loads(f.read())
    print(res)
    print(res['feature'][1])