#! python
 
import string
import base64
from Crypto.PublicKey import RSA  # pip install pycryptodome
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.Hash import SHA256
 
str_data = "{\n  \"msg\":\"hello\"\n}/oauth2/test_sign1707119422"
 
## import RSA public/private key
rsa_private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIICWgIBAAKBgQCaGp1EvvBWMTwwhLFGQ/oCBMRIR8PTVqUThWKS6dJvvo0Y47Nt\n6h+9nZYL7cmfPG2C0stJKCFT+8i0Hny73ijdQL0VvIdEHj8/fq2MUpS0WB2ApsuY\n6xnuyD8mJyueCOtu6zXVg2KqMQQXB45gmTTL0OKeSCrR2RJ5+/kXksMNcwIDAQAB\nAn93R1EpNLHwbbfsTyDc5LLxFBpKNbAo8m6neSX8m/yYsycuAScSay2iIG2rTKoC\nKJeYUwyCAaaWBXZnVKKXykR69wpAMPl2xcesPXJ0rFVlC4xC9eYZ1tipm8hRiqA8\nNmuLcadwk63woHWyblq/XAGUxCSgtNIqArmbX2JiRJbBAkEAtfzfc4k1ti/iS4gU\n2HZsdmi1TmfUhQ4WvLEVDv9MyhxMPHdUZvZpZu67gGg5mO5w4raiIadEb2PDCKK7\n4eujKQJBANjGstxNi+1X40lQ09BeEWwhPb27eH+M6xKl+MSS7wCIUpAiMKgJCUVJ\nz9G1t3w+sbq2GnLhpJf9Dxf0LeFKOzsCQGg1J2KKBAaRvrvPbVhR32OiK4d87vVN\njvl3UP6oc7kboQ/SqLLYkJxPQXCSvcBzcJJxT7+Dfy1la62LOZhxDJkCQBtsj8Yl\nHVWqb7ufuRw8OlIGpovxQp5IUpjqXF1qBUh49pD7clJfykd0vhDWv169g7iOPyxX\ndX4w6o7qOj+tJ28CQQCIXu+Xp7RRAOazZGSxyw/WwEDt0n8yd2GKuAiqH64CIM7M\nubtT9mgayfkR6VH2k0N5KezB1EjmeICsBQY2tO7o\n-----END RSA PRIVATE KEY-----"
rsa_public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCaGp1EvvBWMTwwhLFGQ/oCBMRI\nR8PTVqUThWKS6dJvvo0Y47Nt6h+9nZYL7cmfPG2C0stJKCFT+8i0Hny73ijdQL0V\nvIdEHj8/fq2MUpS0WB2ApsuY6xnuyD8mJyueCOtu6zXVg2KqMQQXB45gmTTL0OKe\nSCrR2RJ5+/kXksMNcwIDAQAB\n-----END PUBLIC KEY-----"
 
## rsa256 generate signature
digest = SHA256.new()
digest.update(str_data.encode('utf-8')) # digest of the data
print("str_sha256:", digest.hexdigest())
 
signer = Signature_pkcs1_v1_5.new(RSA.importKey(rsa_private_key))
sign = signer.sign(digest) # encrypt digest of the data by rsa alg
signature = base64.b64encode(sign)
print("signature:", signature)
 
## rsa256 verify signature
verifier = Signature_pkcs1_v1_5.new(RSA.importKey(rsa_public_key))
verified = verifier.verify(digest, base64.b64decode(signature))
print("verifed:", verified)