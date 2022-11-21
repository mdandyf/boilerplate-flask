from flask import request, g
from functools import wraps
from jwt import DecodeError
from core.response import ResponseSuccess, ResponseFailed
from utility.jwt import jwt_decode, jwt_encode

from model.Client import Client
from model.User import User
from schema.user import UserSchema

class Auth():
    @staticmethod
    def client_restriction(func):
        @wraps(func)
        def client_auth(*args, **kwargs):
            if 'Client-ID' not in request.headers:
                return ResponseFailed('Unauthorized', 401)

            client_id = request.headers.get('Client-ID')
            client_secret = request.headers.get('Client-Secret')

            client = Client.get_by_auth(client_id, client_secret)
            if not client:
                return ResponseFailed('Unauthorized', 401)

            g.client = client
            return func(*args, **kwargs)

        return client_auth

    @staticmethod
    def user_restriction(func):
        @wraps(func)
        def user_auth(*args, **kwargs):
            if 'Access-Token' not in request.headers:
                return ResponseFailed('Unauthorized', 401)

            token = request.headers.get('Access-Token')
            try:
                payload = jwt_decode(token)
                user = User.get_by_id(payload['sub'])
                if not user:
                    return ResponseFailed('Unauthorized', 401)
                g.user = UserSchema().dump(user)
            except DecodeError as e:
                return ResponseFailed('Unauthorized', 401)

            return func(*args, **kwargs)

        return user_auth
