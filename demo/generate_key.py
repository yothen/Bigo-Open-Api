#! python
import string
import base64
from Crypto.PublicKey import RSA  # pip install pycryptodome
 
## generate RSA public/private key
rsa_key_length = 2048
rsa_key = RSA.generate(rsa_key_length)
rsa_private_key = rsa_key.export_key()
rsa_public_key = rsa_key.publickey().export_key()
 
print("\nrsa_private_key:\n", rsa_private_key)
print("\nrsa_private_key_base64:\n", base64.b64encode(rsa_private_key.encode('utf-8')))
print("\nrsa_public_key:\n", rsa_public_key)
print("\nrsa_public_key_base64:\n", base64.b64encode(rsa_public_key.encode('utf-8')))