from Crypto.PublicKey import RSA


def generate_key_pair():
    key = RSA.generate(2048)
    bin_priv_key = key.exportKey('OpenSSH')
    bin_pub_key = key.publickey().exportKey('OpenSSH')
    priv_key = RSA.import_key(bin_priv_key)
    pub_key = RSA.importKey(bin_pub_key)
    return priv_key, pub_key