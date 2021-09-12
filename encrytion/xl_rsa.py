from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA


class Rsa:
    def __init__(self, pubkey, e=65537):
        """
        create a Rsa object
        :param pubkey:
            public key
            It can be an integer or a string.
            When it is a string, its format is either
            a hexadecimal string or a PEM format
        :param e:
            The general value is 65537.
        """
        if isinstance(pubkey, int):
            self.key = RSA.RsaKey(n=pubkey, e=e)

        else:
            if not isinstance(pubkey, str):
                raise ValueError('pubkey must be str or int.')

            if '----' in pubkey:
                try:
                    self.key = RSA.import_key(pubkey)
                except Exception as e:
                    print(e)
            else:
                if pubkey == pubkey.lower():
                    pubkey = int(pubkey, 16)
                    self.key = RSA.RsaKey(n=pubkey, e=e)
                else:
                    pubkey = '-----BEGIN PUBLIC KEY-----\n' + pubkey + '\n-----END PUBLIC KEY-----'
                    try:
                        self.key = RSA.import_key(pubkey)
                    except Exception as e:
                        print(e)

    def encrypt(self, data):
        """
        encrypted data by rsa
        :param data: Plaintext
        :return: Binary ciphertext
        """
        cipher_rsa = PKCS1_OAEP.new(self.key)
        return cipher_rsa.encrypt(data)

    def decrypt(self, data):
        """
        decrypt data by rsa
        :param data: encrypted data
        :return: utf-8 text
        """






if __name__ == '__main__':

    rsa = Rsa(pubkey=open("public.pem").read())
    res = rsa.encrypt('我是WeFi'.encode())
    print(res)
    # print(len(res))