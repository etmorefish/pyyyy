import hashlib
# sha1 sha256 sha512 一样的用法
info = '2020加密乘车！'
m = hashlib.md5(info.encode())  # 注意传入数据一定是二进制数据
res1 = m.hexdigest()  # 输出散列字符串
print(res1)
res2 = m.digest()   # 输出二进制数据

# 大数据的hash
# big_m = hashlib.md5()
# with open('movie.avi', 'rb') as f:
#     for line in f:
#         big_m.update(line)      # 循环追加
# print(big_m.hexdigest())