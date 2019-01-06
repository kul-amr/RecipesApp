import uuid
from app.main import db
from app.main.model.ingredient import Ingredient


def create_ingredient(data):

    ingredient = Ingredient.query.filter_by(name=data['ingredient_name']).first()

    if not ingredient:
        new_ingredient = Ingredient(ingredient_id=str(uuid.uuid4())[:8],
                            name=data['name'])

        db.session.add(new_ingredient)
        db.session.commit()

        resp_obj = {'status':'success',
                    'message':'ingredient created successfully'}

        return resp_obj, 200
    else:
        resp_obj = {'status': 'fail',
                    'message': 'ingredient already exists'}

        return resp_obj, 400


def get_ingredient(ingredient_id=None,ingredient_name=None):

    if ingredient_id is not None:
        return Ingredient.query.filter_by(ingredient_id=ingredient_id).first()
    elif ingredient_name is not None:
        return Ingredient.query.filter_by(name=ingredient_name).first()
    else:
        return None


def get_ingredients():

    return Ingredient.query.all()