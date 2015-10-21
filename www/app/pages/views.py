from app import app
from flask import render_template, request

from app.auth import login

@app.route("/")
def home():
    auth_cookie = request.cookies.get(app.cfg['auth_cookie_name'])

    if (login.check_login(auth_cookie)):
        user = app.cfg['user']
    else:
        user = 0

    return render_template('page_home.html', user=user)

@app.route("/about/")
def about():
    return render_template('page_about.html')
