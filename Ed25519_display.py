#documentation here: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/#
import cryptography
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
message = b"my authenticated message"
#encryption_key = "encryption key"
private_key = Ed25519PrivateKey.generate()
signature = private_key.sign(message)
public_key = private_key.public_key()

try:
    public_key.verify(signature, b"my authenticated message")    
    print("Singature valid!\n\n")
except cryptography.exceptions.InvalidSignature: 
    print("Signature invalid!\n\n")
except Exception as e:
    print("What?: "+e)


    #Made from this: https://stackoverflow.com/questions/32804053/how-to-load-a-rsa-public-key-using-pythons-cryptography-module


ascii_pubk = public_key.public_bytes(cryptography.hazmat.primitives.serialization.Encoding.PEM, cryptography.hazmat.primitives.serialization.PublicFormat.SubjectPublicKeyInfo)
#https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/#cryptography.hazmat.primitives.serialization.Encoding
#https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/#cryptography.hazmat.primitives.asymmetric.ed25519.Ed25519PrivateKey.private_bytes
#https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/#cryptography.hazmat.primitives.serialization.KeySerializationEncryption
ascii_prik = private_key.private_bytes(cryptography.hazmat.primitives.serialization.Encoding.PEM, cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8, cryptography.hazmat.primitives.serialization.NoEncryption())#BestAvailableEncryption(encryption_key)))


print("Private key is: \n"+str(ascii_prik))
print("Public key is: \n"+str(ascii_pubk))
print("Message is: "+str(message))
print("Signature is: "+str(signature.encode('hex')))