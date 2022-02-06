import base64


def encoder(password):
    encoded_password = base64.b64encode(password.encode("urf-8"))
    return encoded_password


def decoder(encoded_password):
    password = base64.b64decode(encoded_password)
    return password

