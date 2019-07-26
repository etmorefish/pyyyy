from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

class Rsa:
    def __init__(self, pubkey, e=65537):
        # self.key = RSA.RsaKey(n=pubkey,e=e)
        if isinstance(pubkey, int):                       #判断是否为int
            self.key = RSA.RsaKey(n=pubkey, e=e)
        else:
            if not isinstance(pubkey, str):               #判断是否为str
                raise ValueError('pubkey must be str or int.')

            if '----' in pubkey:
                try:
                    self.key = RSA.import_key(pubkey)
                except Exception as e:
                    print(e)
            else:
                if pubkey == pubkey.lower() or pubkey == pubkey.lower():
                    pubkey = int(pubkey, 16)
                    self.key = RSA.RsaKey(n=pubkey, e=e)
                else:
                    pubkey = '-----BEGIN PUBLIC KEY-----\n' + pubkey + '\n-----END PUBLIC KEY-----'  #pingjie
                    try:
                        self.key = RSA.import_key(pubkey)
                    except Exception as e:
                        print(e)

    def encrypt(self, date):
        cipher_rsa = PKCS1_OAEP.new(self.key)
        return cipher_rsa.encrypt(date)

if __name__ == '__main__':
    rsa = Rsa(pubkey=open('public.pem').read())
    msg = input('输入要加密的信息:').encode()
    msg = rsa.encrypt(msg)
    print(msg)
    print(len(msg))