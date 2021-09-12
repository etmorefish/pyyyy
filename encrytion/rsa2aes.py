import binascii

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES

# AES案例
# 16个字节的密码
key = b'1234567890123456'
data = '我是lxxl'.encode()
class Aes:
    def __init__(self, key):
        self.key = key
        # self.data = data
        self.cipher = AES.new(self.key, mode=AES.MODE_EAX)


    def encryptAes(self, data):
        # 创建加密对象
        # cipher = AES.new(key, mode=AES.MODE_EAX)
        # encrytion

        msg = self.cipher.encrypt(data)
        print(msg)
        return msg

    def decryptAes(self, data):
        # 解密 过程
        # 创建一个新的密码对象
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.cipher.nonce)
        # msg = self.cipher.decrypt(self.data)
        msg = cipher.decrypt(data)
        print(msg)
        # print(msg.decode('utf-8'))
        return msg

q = Aes(key)
msg = q.encryptAes(data)
q.decryptAes(msg)

print('----------')

def generate_key():
    """
    生成密钥对
    :return:
    """
    key = RSA.generate(1025)
    private_key = key.export_key()
    print(private_key)
    with open('prikey.pem', 'wb') as f:
        f.write(private_key)

    public_key = key.publickey().export_key()
    print(public_key)
    with open('pubkey.pem', 'wb') as f:
        f.write(public_key)

# generate_key()

def encrypt():
    """
    加密
    :return:
    """
    public_key = RSA.import_key(open('pubkey.pem', 'r').read())
    data = '加密传输的信息'.encode()
    cipher = PKCS1_OAEP.new(public_key)
    msg = cipher.encrypt(data)
    # print(msg)
    # print(binascii.b2a_hex(msg))
    return msg

# encrypt()

def decrypt():
    """
    解密
    :return:
    """
    private_key = RSA.import_key(open('prikey.pem').read())
    msg = encrypt()
    print(f'加密过的信息： {msg}')
    cipher = PKCS1_OAEP.new(private_key)
    res = cipher.decrypt(msg).decode('utf-8')
    print("解密: ",res)
    return res


decrypt()