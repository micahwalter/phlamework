from flask import Flask
from flask.ext.mysql import MySQL

app = Flask(__name__)
app.debug = True

## global config stuff ...
app.cfg = {}
app.cfg['user'] = 1
app.cfg['auth_cookie_name'] = 'a'
app.cfg['crypto_cookie_secret'] = 'S33KRET'
app.cfg['auth_cookie_domain'] = 'localhost'

mysql = MySQL()

# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'phlamework'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# MySQL connection
app.db = mysql.connect().cursor()

## import all the things...
from pages import views
from auth import views
