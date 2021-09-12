from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
# 16个字节的密码
key = b'1234567890123456'
print(key)
cipher = AES.new(key, AES.MODE_EAX)
data = '这是一段被加密的信息'.encode()
ciphertext, tag = cipher.encrypt_and_digest(data)
print(cipher.nonce, tag, ciphertext)
file_out = open("encrypted", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()

# b'\xf9\xac[\x03h\xf19m?\xbaH\x9e\x7f\xd1\xc3\x83'
# b'\x1f\xb0\xad\tw?\x1e\xc8\xe2dX\xb3@`Q\x8d'
# b'\x8eS\xd6\x9c\x85\x0fC\xf7\rUQa>\xbc>\x86\xe1\xb5|\xe6\xab\x90]\xd8\x8f\x95\xa9w\n\xfa'