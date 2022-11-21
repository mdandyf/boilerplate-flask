from flask import request, Blueprint, g
from marshmallow import ValidationError

from core.response import ResponseSuccess, ResponseFailed
from utility.jwt import jwt_encode

from schema.auth import RegisterSchema, LoginSchema
from schema.user import UserSchema
from model.User import User
from middleware.Auth import Auth

auth_handler = Blueprint('auth_handler', __name__)

@auth_handler.route('/register', methods=['POST'])
def register():
    try:
        req_data = request.get_json()
        data = RegisterSchema().load(req_data)
    except ValidationError as e:
        return ResponseFailed(e.messages, 422)

    user_in_db = User.get_by_email(data.get('email'))
    if user_in_db:
        return ResponseFailed('User already exist, please choose another email', 422)

    user = User(data)
    user.save()

    transform = UserSchema().dump(user)
    token = jwt_encode(transform.get('id'))

    return ResponseSuccess({
        'token_type': 'Bearer',
        'access_token': token
    }, 201)


@auth_handler.route('/login', methods=['POST'])
def login():
    try:
        req_data = request.get_json()
        data = LoginSchema().load(req_data)
    except ValidationError as e:
        return ResponseFailed(e.messages, 422)

    user = User.get_by_email(data.get('email'))
    if not user:
        return ResponseFailed('Unauthorized', 401)
    if not user.check_hash(data.get('password')):
        return ResponseFailed('Unauthorized', 401)

    transform = UserSchema().dump(user)
    token = jwt_encode(transform.get('id'))

    return ResponseSuccess({
        'token_type': 'Bearer',
        'access_token': token
    }, 200)


@auth_handler.route('/user', methods=['GET'])
@Auth.user_restriction
def me():
    return ResponseSuccess(g.user, 200)
