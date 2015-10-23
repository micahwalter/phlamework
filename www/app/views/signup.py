from app import app
from flask import render_template, request, redirect

from app.include import login
from app.include import users

@app.route("/signup/", methods=['GET', 'POST'])
def signup():

    auth_cookie = request.cookies.get(app.cfg['auth_cookie_name'])
    if (login.check_login(auth_cookie)):
        return redirect("/")

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        #
        # all fields are in order?
        #

        if ( (not len(email)) or (not len(password)) or (not len(username))):
            error = {"error_missing":1}
            return render_template("page_signup.html", error=error)

        #
        # email available
        #

        if users.is_email_taken(email):
            error = {"error_email_taken":1}
            return render_template("page_signup.html", error=error)

        #
        # username available
        #

        if users.is_username_taken(username):
            error = {"error_username_taken":1}
            return render_template("page_signup.html", error=error)

        #
        # create account
        #

        user = {"email":email, "password":password, "username":username}
        ret = users.create_user(user)

        if ret:
            user = users.get_user_by_email(ret['email'])
            return login.do_login(user)
        else:
            error = {"error_server":1}
            return render_template("page_signup.html", error=error)

    else:
        ### just show the signup form
        return render_template("page_signup.html")
