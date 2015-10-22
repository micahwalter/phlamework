from app import app
from flask import render_template, request, redirect

from app.include import login
from app.include import crumb

@app.route("/signout/", methods=['GET', 'POST'])
def signout():

    auth_cookie = request.cookies.get(app.cfg['auth_cookie_name'])
    if not login.check_login(auth_cookie):
        return redirect("/")

    #
    # crumb key
    #

    crumb_key = "logout"
    crumb_input = crumb.generate(crumb_key)

    #
    # sign out
    #

    if request.method == 'POST':
        post_crumb = request.form['crumb']
        if not crumb.check(post_crumb, app.cfg['crypto_crumb_secret']):
            return redirect("/")

        return login.do_logout()

    else:
        return render_template("page_signout.html", crumb_input=crumb_input)
