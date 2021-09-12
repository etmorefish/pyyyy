# AES案例
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# 16个字节的密码
key = b'1234567890123456'

nonce = b'\x1d\x1d7ZMX\x89\x82\x93\xde\xf3\xa5VI\x9bs'
msg = b'\xcd\xcd\x9a\xfc^A/\xa4\xe6\xe2\x0f\xcdo\x88\xe1M\x8c\x15>>\xd4;:T,\x02Qz\xfb\xe0'
# 解密 过程
# 创建一个新的密码对象
cipher = AES.new(key, AES.MODE_EAX, nonce)
res = cipher.decrypt(msg)
print(res)
print(res.decode('utf-8'))