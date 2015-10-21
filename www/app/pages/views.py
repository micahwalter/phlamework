from app import app
from flask import render_template, request

from app.auth import login

@app.route("/")
def home():
    return render_template('page_home.html')

@app.route("/about/")
def about():
    return render_template('page_about.html')
