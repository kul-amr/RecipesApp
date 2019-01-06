from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_namespace
from .main.controller.auth_controller import api as auth_namespace
from .main.controller.course_controller import api as course_namespace
from .main.controller.ingredient_controller import api as ingreds_namespace


blueprint = Blueprint('api',__name__)

api = Api(blueprint,
          title='RecipesApp api',
          version='1.0',
          description='Recipesapp api desc')


api.add_namespace(user_namespace, path='/user')
api.add_namespace(auth_namespace,path='/auth')
api.add_namespace(course_namespace, path='/course')
api.add_namespace(ingreds_namespace,path='/ingred')