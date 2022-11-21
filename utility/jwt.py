import os
import jwt

def jwt_encode(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }

    token = jwt.encode(
        payload,
        os.getenv('JWT_SECRET_KEY'),
        'HS256'
    )

    return token


def jwt_decode(token):
    payload = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms='HS256')
    return payload
