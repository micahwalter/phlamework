def encrypt_password(password):

    ### todo ... encrypt the thing...
    return password


def validate_password(password, enc_password):

    test = encrypt_password(password)
    return test == enc_password


def validate_password_for_user(password, user):

    return validate_password(password, user['password'])
