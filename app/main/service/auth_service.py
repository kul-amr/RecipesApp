from app.main.model.user import User
from ..service.invalidtoken_service import save_token


class Auth:

    @staticmethod
    def login_user(data):

        try:

            user = User.query.filter_by(email=data.get('email')).first()

            if user and user.check_password(data.get('password')):

                auth_token = user.encode_auth_token(user_id=user.id)

                if auth_token:
                    res_obj = {'status':'success',
                               'message':'successfully logged in',
                               'Authorization':auth_token.decode()
                               }
                    return  res_obj, 200
            else:
                res_obj = {'status':'fail',
                           'message':'incorrect email or password'}

                return res_obj, 400

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': e
            }
            return response_object, 500


    @staticmethod
    def logout_user(data):

        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''

        if auth_token:
            resp = User.decode_auth_token(auth_token)

            if not isinstance(resp, str):
                return  save_token(auth_token)
            else:
                resp_obj = {'status':'fail',
                            'message':resp}

                return resp_obj, 401

        else:
            resp_obj = {'status':'fail',
                        'message':'invalid auth token'}

            return resp_obj, 401


    @staticmethod
    def get_loggedin_user(req):

        auth_token = req.headers.get('Authorization')

        if auth_token:

            resp = User.decode_auth_token(auth_token)

            if not isinstance(resp,str):
                user = User.query.filter_by(id=resp).first()
                resp_obj = {
                    'status':'success',
                    'data':{
                        'user_id':user.id,
                        'email':user.email,
                        'created_date':user.created_date
                    }
                }

                return resp_obj, 200

            resp_obj = {
                'status': 'fail',
                'message': resp
            }

            return resp_obj, 401
        else:

            resp_obj = {
                'status': 'fail',
                'message': 'invalid auth token'
            }

            return resp_obj, 401