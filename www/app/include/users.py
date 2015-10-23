from app import app
import time
import string
import random

from app.include import passwords

#################################################################
def create_user(user):

    user['password'] = passwords.encrypt_password(user['password'])
    user['created'] = int(time.time())
    user['conf_code'] = ''.join(random.choice(string.ascii_lowercase) for i in range(24))

    sql = "INSERT INTO users (username, email, password, created, conf_code, deleted, confirmed, cluster_id) VALUES ('%s', '%s', '%s', %s, '%s', 0, 0, 1)" % (user['username'], user['email'], user['password'], user['created'], user['conf_code'])

    cursor = app.db.cursor()
    
    try:
        cursor.execute(sql)
        app.db.commit()
    except:
        app.db.rollback()
        return 0

    return user

#################################################################
def get_user_by_id(id):

    sql = "SELECT * FROM users WHERE id=%s" % (id)

    cursor = app.db.cursor()
    cursor.execute(sql)
    return cursor.fetchone()

#################################################################
def get_user_by_email(email):

    sql = "SELECT * FROM users WHERE email='%s'" % (email)

    cursor = app.db.cursor()
    cursor.execute(sql)
    return cursor.fetchone()

#################################################################
def is_email_taken(email):

    sql = "SELECT id FROM users WHERE email='%s'" % (email)

    cursor = app.db.cursor()
    cursor.execute(sql)
    rsp = cursor.fetchone()

    return (rsp is not None)

#################################################################
def is_username_taken(username):

    sql = "SELECT id FROM users WHERE username='%s'" % (username)

    cursor = app.db.cursor()
    cursor.execute(sql)
    rsp = cursor.fetchone()

    return (rsp is not None)
