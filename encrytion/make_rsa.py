from Cryptodome.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
print(private_key)
file_out = open("privates.pem", "wb")
file_out.write(private_key)
public_key = key.publickey().export_key()
print(public_key)
file_out = open("publics.pem", "wb")
file_out.write(public_key)