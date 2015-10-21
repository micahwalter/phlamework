from app import app

#################################################################
def get_user_by_id(id):

    sql = "SELECT * FROM users WHERE id=%s" % (id)

    app.db.execute(sql)
    return app.db.fetchone()

#################################################################
def get_user_by_email(email):

    sql = "SELECT * FROM users WHERE email='%s'" % (email)

    app.db.execute(sql)
    return app.db.fetchone()
