# 3DES案例
from Cryptodome.Cipher import DES3

# 需要24个字节长度的key，一般会随机生成
# 本质上是三次des的key的串联，k1，k2，k3
# 当k1=k2=k3时，DES3降级为DES
key = b'12345678qwertyui123hjsc8'

# 创建一个密码对象
cipher = DES3.new(key, DES3.MODE_CFB)
# 原数据
data = '我是lei'.encode()
# encrytion
msg = cipher.encrypt(data)
print(msg)

# 解密过程
print(cipher.iv)
cipher2 = DES3.new(key, DES3.MODE_CFB, iv=cipher.iv)
# 解密
res = cipher2.decrypt(msg)
print(res)
print(res.decode('utf-8'))

# 文档参考：<https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html
# 2