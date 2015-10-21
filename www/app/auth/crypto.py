from cryptography.fernet import Fernet
import hashlib, base64

######################################################
def encrypt(data, key):

    f = Fernet(key)
    token = f.encrypt(data)

    return base64.b64encode(token)

######################################################
def decrypt(enc_b64, key):

    f = Fernet(key)
    token = base64.b64decode(enc_b64);

    return f.decrypt(token)
