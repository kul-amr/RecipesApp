from flask import request
from flask_restplus import Resource

from ..util.dao import UserDAO
from ..service.user_service import *
from ..util.decorator import *

api = UserDAO.api
_user = UserDAO.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_all_registered_users')
    @api.marshal_list_with(_user,envelope='data')
    # @token_required
    def get(self):
        return get_users()

    @api.response(201,'user created successfully')
    @api.doc('create_new_user')
    @api.expect(_user,validate=True)
    def post(self):
        data =  request.json
        return create_user(data)


@api.route('/<user_id>')
@api.param('user_id','user id')
@api.response(404,'user not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(_user)
    def get(self, user_id):
        user = get_user(user_id=user_id)

        if not user:
            api.abort(404)
        else:
            return user