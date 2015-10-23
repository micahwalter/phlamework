from flask import abort, redirect, make_response, request, g
from app import app
import string
import json

import crypto as crypto
from app.include import users

######################################################
def ensure_loggedout(auth_cookie):
    if not check_login(auth_cookie):
        return do_logout()
    return 1

######################################################
def check_login(auth_cookie):

    if not app.cfg['enable_feature_signin']:
        return 0

    if not auth_cookie:
        if 'user' in g:
            del g.user
        return 0

    auth_cookie = crypto.decrypt(auth_cookie, app.cfg['crypto_cookie_secret'])

    data = auth_cookie.split(':')

    user_id = data[0]
    password = data[1]

    if not user_id:
        return 0

    user = users.get_user_by_id(user_id)

    if not user:
        return 0

    if user['deleted']:
        return 0

    if (user['password'] != password):
        return 0

    g.user = json.dumps(user, indent=4)

    return 1

######################################################
def do_login(user):
    auth_cookie = generate_auth_cookie(user)

    resp = make_response(redirect("/"))
    resp.set_cookie(app.cfg['auth_cookie_name'], auth_cookie)

    return resp


######################################################
def do_logout():

    if 'user' in g:
        del g.user

    resp = make_response(redirect("/"))
    resp.set_cookie(app.cfg['auth_cookie_name'], "", expires=0)

    return resp

######################################################
def generate_auth_cookie(user):
    cookie = ':'.join((str(user['id']), user['password']))
    return crypto.encrypt(cookie, app.cfg['crypto_cookie_secret'])

######################################################
def get_cookie(name):
    #### this isn't necessary since we have to get the cookie at the beginning of each request
    return 0

######################################################
def unset_cookie():
    return 0

######################################################
