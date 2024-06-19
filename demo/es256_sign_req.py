#! python
import time
import base64
import requests
import json
from Crypto.PublicKey import ECC # pip install pycryptodome
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# const value
host = "https://livelbs-test-pro.bigo.sg:1009"
# host = "https://oauth.bigolive.tv"
client_id = "{your-clientid}" 
client_version = 1
ecc_private_key_base64 = "use generate_key.py or generate_key.sh to generate and fill in" #must generate yourself
ecc_public_key_base64 = "use generate_key.py or generate_key.sh to generate and fill in" #must generate yourself

ecc_private_key = base64.b64decode(ecc_private_key_base64)
ecc_public_key = base64.b64decode(ecc_public_key_base64)

def GenerateSign(uri, request, timestamp) :
    str_data = request + uri + str(timestamp)
    print("data:", str_data)
    # sha256 hash
    digest = SHA256.new()
    digest.update(str_data.encode('utf-8'))
    print("base64:", base64.b64encode(digest.digest()))
    # sign with ecc-privatekey
    signer = DSS.new(ECC.import_key(ecc_private_key), 'fips-186-3')
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    print("signature:", signature)
    return signature

def MakeSignedRequest(uri, request) :
    timestamp = int(time.time())
    signature = GenerateSign(uri, request, timestamp)
    url = host + uri
    headers = {}
    headers["Content-type"] = "application/json"
    headers["bigo-client-id"] = client_id
    headers["bigo-timestamp"] = str(timestamp)
    headers["bigo-client-version"] = str(client_version)
    headers["bigo-oauth-signature"] = signature

    response = requests.post(url=url, data=request, headers=headers)
    if response.status_code != 200:
        print("failed. code:%d response:%s" % (response.status_code, response.json()))
        return
    print(response.json())

# 测试case:
# uri: /oauth2/test_sign
# request: {"msg":"hello"}

if __name__ == '__main__':
    uri  = input("输入uri:")
    print(uri)
    print("输入请求，结束后换行输入\"end\"")
    request = ""
    while (1):
        msg = input()
        if msg == "end":
            break
        request = request + msg + "\n"
    
    MakeSignedRequest(uri, request)
