from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256


def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    priv_recipient_key = RSA.import_key(private_key)
    pub_recipient_key = RSA.import_key(public_key)

    return priv_recipient_key, pub_recipient_key





# Usage
signer = PKCS115_SigScheme(priv_recipient_key)
h = SHA256.new()
h.update(b'Hello')
signature = signer.sign(h)

# verify

signer2 = PKCS115_SigScheme(pub_recipient_key)
h = SHA256.new()
h.update(b'Hello')
signer2.verify(h, signature)
