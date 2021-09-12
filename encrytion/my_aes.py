# AES案例
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# 16个字节的密码
# key = b'1234567890123456'
key = get_random_bytes(16)
print(key, type(key))
# 创建加密对象
cipher = AES.new(key, mode=AES.MODE_EAX)
data = '我是lxxl'.encode()
# encrytion
msg = cipher.encrypt(data)

print(msg, type(msg))  # b'\x83\xb9u\x8c\xde\x08\ru1a'
# 解密 过程
# 创建一个新的密码对象
cipher2 = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
res = cipher2.decrypt(msg)
print(res, type(res))
print(res.decode('utf-8'))
'''
文档参考：<https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html>

'''
# 3