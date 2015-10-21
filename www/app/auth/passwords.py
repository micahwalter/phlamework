import bcrypt

######################################################
def encrypt_password(password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

######################################################
def validate_password(password, enc_password):
    return enc_password == bcrypt.hashpw(password.encode('utf-8'), enc_password)

######################################################
def validate_password_for_user(password, user):

    return validate_password(password, user['password'])
