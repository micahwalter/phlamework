import hashlib, base64

######################################################
def encrypt(data, key):

    key = hashlib.sha256(key)

    return base64.b64encode(data)

######################################################
def decrypt(enc_b64, key):

	dec = base64.b64decode(enc_b64);
	# $dec = mcrypt_decrypt(MCRYPT_RIJNDAEL_256, $key, $enc, MCRYPT_MODE_ECB);
	return dec
