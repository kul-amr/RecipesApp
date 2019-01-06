from flask import request
from flask_restplus import Resource

from app.main.service.auth_service import Auth
from ..util.dao import AuthDAO


api = AuthDAO.api
user_auth = AuthDAO.user_auth



@api.route('/login')
class UserLogin(Resource):

    @api.doc('user login')
    @api.expect(user_auth,validate=True)
    def post(self):

        post_data = request.json

        return Auth.login_user(post_data)


@api.route('/logout')
class UserLogout(Resource):

    @api.doc('user logout')
    def post(self):

        auth_header=  request.headers.get('Authorization')

        return Auth.logout_user(data=auth_header)
