import binascii

from Cryptodome.Cipher import AES

# 16个字节的密码
key = b'1234567890123456'
# 创建加密对象
cipher = AES.new(key, mode=AES.MODE_EAX)
data = '这是一段被加密的信息'.encode()
# encrytion
msg = cipher.encrypt(data)
print(cipher.nonce)
# b'\x1d\x1d7ZMX\x89\x82\x93\xde\xf3\xa5VI\x9bs'
print(msg)
print(type(msg))

# b'\xcd\xcd\x9a\xfc^A/\xa4\xe6\xe2\x0f\xcdo\x88\xe1M\x8c\x15>>\xd4;:T,\x02Qz\xfb\xe0'
