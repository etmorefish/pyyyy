# DES 使用
import binascii
from Cryptodome.Cipher import DES
key = b'-8B key-'               # key 必须是8个字节64位

# 创建一个密码对象
# iv 参数也需要是一个8字节64位的二进制数,初始化向量
# DES.MOD_OFB加密模式

cipher = DES.new(key, DES.MODE_OFB, iv=b'12345079')
# 待加密数据
data = '毛雷是python大神'.encode()
# encrytion
msg = cipher.encrypt(data)
# 输出二进制数据
print(msg)
# 输出16进制字符串
print(binascii.b2a_hex(msg))

# 解密过程

# 创建一个新的密码对象
# 模式，key，iv 和加密过程对应
print(cipher.iv)
cipher2 = DES.new(key, iv=cipher.iv, mode=DES.MODE_OFB)

# 解密
res = cipher2.decrypt(msg)
# 解码成明文字符串
print(res.decode('utf-8'))

# 文档参考：<https://pycryptodome.readthedocs.io/en/latest/src/cipher/des.html>

# DES加密了解就好，几乎没人使用了。
# 1