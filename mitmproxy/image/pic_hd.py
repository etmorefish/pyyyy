# -*- coding: utf-8 -*-
# @Time    : 19-7-25 下午2:17
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : pic_hd.py
# @Software: PyCharm


import os

# for pic in pics:
#     print(pic)
#     print(os.path.join('.',pic))

count = 0
new = []
for root,dirs,files in os.walk('.'):
    for file in files:
        count += 1
        print(new)
        # print(file,end=' ')
        if '_hd' in file:
            new.append(file)


        

if __name__ == '__main__':
    # filenames()
    print(count)
    print(new,count(new))