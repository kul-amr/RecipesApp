from app.main import db
from app.main.model.invalidToken import InvalidToken


def save_token(token):

    invalid_token = InvalidToken(token=token)

    try:
        db.session.add(invalid_token)
        db.session.commit()

        res_obj = {'status':'success','message':'successfully logged out'}

        return res_obj, 200
    except Exception as e:
        res_obj = {'status': 'fail', 'message': e}

        return res_obj, 400
