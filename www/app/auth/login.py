from flask import abort, redirect, make_response, request
from app import app
import string

import crypto as crypto
from app.users import users

######################################################
def ensure_loggedin():
    if 'user' in app.cfg:
        return 1
    else:
        return redirect("/signin/")

######################################################
def ensure_loggedout(auth_cookie):
    check_login(auth_cookie)
    return 0

######################################################
def check_login(auth_cookie):

    if not app.cfg['enable_feature_signin']:
        return 0

    if not auth_cookie:
        if 'user' in app.cfg:
            del app.cfg['user']
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

    app.cfg['user'] = user

    return 1

######################################################
def do_login(user):
    auth_cookie = generate_auth_cookie(user)

    resp = make_response(redirect("/"))
    resp.set_cookie(app.cfg['auth_cookie_name'], auth_cookie)

    return resp


######################################################
def do_logout():
    return 0

######################################################
def generate_auth_cookie(user):
    cookie = ':'.join((str(user['id']), user['password']))
    return crypto.encrypt(cookie, app.cfg['crypto_cookie_secret'])

######################################################
def get_cookie(name):
    #cookie = request.cookies.get('a')
    #print cookie

    #cookie = request.cookies.get(name)
    #print cookie
    return 0

######################################################
def unset_cookie():
    return 0

######################################################
