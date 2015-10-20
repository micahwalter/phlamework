from app import app
from flask import render_template

@app.route("/")
def home():

    ### testing the connectiob to the DB
    app.db.execute("SELECT * FROM test")
    data = app.db.fetchall()

    return render_template('page_home.html', data=data)

@app.route("/about/")
def about():
    return render_template('page_about.html')
