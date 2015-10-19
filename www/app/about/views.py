from app import app
from flask import render_template

@app.route("/about/")
def about():
    #return "About this thing!"
    return render_template('page_about.html')
