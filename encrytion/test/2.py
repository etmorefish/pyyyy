from Crypto.Cipher import AES

file_in = open("encrypted", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
key = b'\xb7\xa0\x80j.\x9d|i\x93\x9es\xce3i\xb45'

key = b'1234567890123456'
nonce = b'\xf9\xac[\x03h\xf19m?\xbaH\x9e\x7f\xd1\xc3\x83'
tag = b'\x1f\xb0\xad\tw?\x1e\xc8\xe2dX\xb3@`Q\x8d'
ciphertext = b'\x8eS\xd6\x9c\x85\x0fC\xf7\rUQa>\xbc>\x86\xe1\xb5|\xe6\xab\x90]\xd8\x8f\x95\xa9w\n\xfa'
# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data.decode())