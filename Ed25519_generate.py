#documentation here: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/#
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
private_key = Ed25519PrivateKey.generate()
signature = private_key.sign(b"my authenticated message")
public_key = private_key.public_key()
try:
    public_key.verify(signature, b"my authenticated mes sage")
    print("Authed sucess")
except Exception as error:
    
    print("Auth Failure: "+str(error))