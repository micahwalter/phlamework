from flask import Flask
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)
app.debug = True

## global config stuff ...
app.cfg = {}

app.cfg['auth_cookie_name'] = 'a'
app.cfg['crypto_cookie_secret'] = 'XWvXBujpxWtm9YYl3Kt2xo4rqp_wEXKB8GI1CxZJ4wg='
app.cfg['auth_cookie_domain'] = 'localhost'

app.cfg['enable_feature_signin'] = 1;

database = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "phlamework",
    cursorclass=MySQLdb.cursors.DictCursor)

app.db = database.cursor()

## import all the things...
from pages import views
from auth import views

#from auth import login
#login.check_login()
