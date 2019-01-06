import uuid
import datetime as dt
from app.main import db
from app.main.model.user import User


def create_user(data):

    user = User.query.filter_by(email=data['email']).first()

    if not user:
        new_user = User(user_id=str(uuid.uuid4())[:8],
                        email=data['email'],
                        username = data['username'],
                        password=data['password'],
                        created_date=dt.datetime.utcnow())
        save_changes(new_user)

        # response_obj = {'status':'success',
        #                 'message':'user created successfully'}

        return generate_token(new_user)
    else:
        response_obj = {'status': 'fail',
                        'message': 'user already exists'}

        return response_obj, 409


def get_users():

    return User.query.all()

def get_user(user_id):

    return User.query.filter_by(user_id=user_id).first()

def save_changes(data):

    db.session.add(data)
    db.session.commit()


def generate_token(user):
    try:

        auth_token = user.encode_auth_token(user.id)

        res_obj = {
            'status': 'success',
            'message': 'Successfully created.',
            'Authorization': auth_token.decode()
        }
        return res_obj, 201

    except Exception as e:
        res_obj = {
            'status': 'fail',
            'message': e
        }
        return res_obj, 400