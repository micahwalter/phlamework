from app import app
from flask import render_template, request

import login as login
import passwords as passwords

@app.route("/signin/", methods=['GET', 'POST'])
def signin():

    login.ensure_loggedout()

    #
    # try and sign in
    #

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        #
        # required fields?
        #

        if ((not len(email)) or (not len(password))):
            error = {"error_missing":1}
            return render_template("page_signin.html", error=error)

        #
        # user exists
        #

        ## get the user by email address
        ## user = users.get_user_by_email(email)
        ## this is a fake user
        user = {"id":1, "username":"test", "email":email, "password":"test", "deleted":0}

        if (not user):
            error = {"error_nouser":1}
            return render_template("page_signin.html", error=error)

        #
        # user deleted
        #

        if (user['deleted']):
            error = {"error_deleted":1}
            return render_template("page_signin.html", error=error)

        #
        # password matches
        #

        if (not passwords.validate_password_for_user(password, user)):
            error = {"error_password":1}
            return render_template("page_signin.html", error=error)

        #
        # it's all good - sign in
        #

        return login.do_login(user)

    else:
        ### just show the login form
        return render_template("page_signin.html")