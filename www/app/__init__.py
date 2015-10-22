from flask import Flask, request
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)
app.debug = True ### Set this to false for production apps

## global config stuff ...
app.cfg = {}

app.cfg['auth_cookie_name'] = 'a'
app.cfg['auth_cookie_domain'] = 'localhost'

### Important!!!  -- Use bin/generate_secret.py to make a crypto key of your own.
app.cfg['crypto_cookie_secret'] = 'XWvXBujpxWtm9YYl3Kt2xo4rqp_wEXKB8GI1CxZJ4wg='
app.cfg['crypto_crumb_secret'] = 'XWvXBujpxWtm9YYl3Kt2xo4rqp_wEXKB8GI1CxZJ4wg='

### Database connnection info
database = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "phlamework",
    cursorclass=MySQLdb.cursors.DictCursor)

### Bootstrap the DB connection
app.db = database.cursor()

### Feature flags
app.cfg['enable_feature_signin'] = 1;

### Do these things on every page load
from app.include import login

@app.before_request
def init():
    app.cfg['script_name'] = request.path
    app.cfg['User-Agent'] = request.headers.get('User-Agent')
    auth_cookie = request.cookies.get(app.cfg['auth_cookie_name'])
    login.check_login(auth_cookie)

## import all the views...
from views import home
from views import about
from views import signin
from views import signout
