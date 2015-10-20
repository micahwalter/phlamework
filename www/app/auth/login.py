from flask import abort, redirect, make_response
from app import app

import crypto as crypto

######################################################
def ensure_loggedin():
    if app.cfg['user']:
        return 1
    else:
        return redirect("/signin/")

######################################################
def ensure_loggedout():
    return 0

######################################################
def check_login():
    return 0

######################################################
def do_login(user):
    auth_cookie = generate_auth_cookie(user)

    resp = make_response(redirect("/"))
    resp.set_cookie(app.cfg['auth_cookie_domain'], auth_cookie)

    return resp


######################################################
def do_logout():
    return 0

######################################################
def generate_auth_cookie(user):
    cookie = ':'.join((str(user['id']), user['password']))
    return crypto.encrypt(cookie, app.cfg['crypto_cookie_secret'])

######################################################
def get_cookie():
    return 0

######################################################
def unset_cookie():
    return 0

######################################################
