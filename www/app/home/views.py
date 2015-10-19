from app import app
from flask import render_template

@app.route("/")
def home():
    #return "About this thing!"
    return render_template('page_home.html')
