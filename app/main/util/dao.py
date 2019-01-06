from flask_restplus import Namespace, fields


class UserDAO:

    api = Namespace('user',description='user related operations')
    user = api.model('user',{
        'email':fields.String(required=True,description='user email'),
        'username': fields.String(required=True, description='username'),
        'password': fields.String(required=True, description='user password')
    })


class AuthDAO:

    api = Namespace('auth', description='auth related operations')
    user_auth = api.model('auth_dets', {
        'email': fields.String(required=True, description='user email'),
        'password': fields.String(required=True, description='user password')
    })


class CourseDAO:


    api = Namespace('course', description='course related operations')
    course = api.model('course', {
        'course_title': fields.String(required=True, description='course title')
    })



class IngredientDAO:


    api = Namespace('ingredient', description='ingredient related operations')
    ingredient = api.model('ingredient', {
        'name': fields.String(required=True, description='ingredient name')
    })