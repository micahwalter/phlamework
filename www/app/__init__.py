from flask import Flask

app = Flask(__name__)
app.debug = True

## global config stuff ...
app.cfg = {}
app.cfg['user'] = 1
app.cfg['auth_cookie_name'] = 'a'
app.cfg['crypto_cookie_secret'] = 'S33KRET'
app.cfg['auth_cookie_domain'] = 'localhost'

## import all the things...
from pages import views
from auth import views
