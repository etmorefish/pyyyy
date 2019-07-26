# AES案例
from Cryptodome.Cipher import AES
# 16个字节的密码
key = b'1234567890123456'
# 创建加密对象
cipher = AES.new(key, mode=AES.MODE_EAX)
data = '我是心蓝'.encode()
# encrytion
msg = cipher.encrypt(data)

print(msg)
# 解密 过程
# 创建一个新的密码对象
cipher2 = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
res = cipher2.decrypt(msg)
print(res.decode('utf-8'))
'''
文档参考：<https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html>

'''