from flask import Flask

app = Flask(__name__)
app.debug = True

from home import views
from about import views
