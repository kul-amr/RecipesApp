from flask import request
from flask_restplus import Resource

from ..util.dao import IngredientDAO
from ..service.ingredient_service import *
from ..util.decorator import *

api = IngredientDAO.api
_ingredient = IngredientDAO.ingredient


@api.route('/')
class IngredientList(Resource):
    @api.doc('list_of_all_ingredients')
    @api.marshal_list_with(_ingredient,envelope='data')
    # @token_required
    def get(self):
        return get_ingredients()

    @api.response(201,'ingredient created successfully')
    @api.doc('create_new_course')
    @api.expect(_ingredient,validate=True)
    def post(self):
        data =  request.json
        return create_ingredient(data)


@api.route('/<ingredient_id>')
@api.param('ingredient_id')
@api.response(404,'ingredient not found')
class Ingredient(Resource):
    @api.doc('get_ingredient_with_id')
    @api.marshal_with(_ingredient)
    def get(self, ingredient_id):
        ingredient = get_ingredient(ingredient_id=ingredient_id)

        if not ingredient:
            api.abort(404)
        else:
            return ingredient


@api.route('/<ingredient_name>')
@api.param('ingredient_name')
@api.response(404,'ingredient not found')
class Ingredient(Resource):
    @api.doc('get_ingredient_with_name')
    @api.marshal_with(_ingredient)
    def get(self, ingredient_name):
        ingredient = get_ingredient(ingredient_name=ingredient_name)

        if not ingredient:
            api.abort(404)
        else:
            return ingredient