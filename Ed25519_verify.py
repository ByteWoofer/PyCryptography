#Made from this: https://stackoverflow.com/questions/32804053/how-to-load-a-rsa-public-key-using-pythons-cryptography-module

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
raw_public_key = '-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAmtca61ILHEp4tu8S/ul93OzG1Ikys5ZhOf1FL6QepPg=\n-----END PUBLIC KEY-----\n'
signature = '\xaf\xd2R[\xe8\xe2\x00\xe3l\xbd8\x1e\x7f\x8f\xda6\xa2\x82\xb2R\nUl\xa7\xe2\x90\xbb\x8d\xb4\x15\xf0p\xf5\xd9/V\xb0\xfan\x18\x03 \xc5\x0b\x16Qr\xa0[\xff\x82\x00\xf0\xe8B#6&\rj\xa5d,\n'
public_key = load_pem_public_key(raw_public_key, default_backend())
try:
    public_key.verify(signature, b'ThisIsVerified')
    print("signature verification passed")
except:
    print("signature verification failed")