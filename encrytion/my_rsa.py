from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
data = '我是心蓝哈哈哈哈'.encode()

# 导入公钥
public_key = RSA.import_key(open("public.pem").read())
# 创建一个密码对象
cipher_rsa = PKCS1_OAEP.new(public_key)

# 加密
msg = cipher_rsa.encrypt(data)
print(msg)
# 导入私钥
private_key = RSA.import_key(open("private.pem").read())
cipher_rsa = PKCS1_OAEP.new(private_key)
# 解密
res = cipher_rsa.decrypt(msg)
print(res.decode('utf-8'))