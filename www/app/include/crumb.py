from app import app
import time
import hashlib
import string


######################################################
def generate(key, target=''):

    base = get_base(key, target)
    thetime = int(time.time())

    ## snowman = "\xE2\x98\x83"

    hashed = get_hash(base+str(thetime))

    return str(thetime) + "-" + hashed #+ "-" + snowman

######################################################
def get_base(key, target=''):

    if not target:
        target = app.cfg['script_name']

    base = ':'.join((key, app.cfg['User-Agent'], target))

    ### If they are signed in...?

    return base

######################################################
def get_hash(thestring, len=5):

    m = hashlib.sha1()
    m.update(app.cfg['crypto_crumb_secret'] + thestring)
    hashed = m.hexdigest()

    return hashed[:len]


######################################################
def check(test, key, ttl=0, target=''):
	return validate(test, key, ttl, target)

######################################################
def validate(test, key, ttl, target):

    data = test.split('-')

    thetime = data[0]
    hashed = data[1]

    base = get_base(key, target)
    hash_test = get_hash(base+thetime)

    if ( len(hash_test) != len(hashed)):
        return 0

    return 1
