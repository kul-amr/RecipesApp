from .. import db
import datetime as dt



class InvalidToken(db.Model):

    __tablename__ = 'invalid_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    token = db.Column(db.String(500), unique=True,nullable=False)
    invalidated_on = db.Column(db.DateTime, nullable=False)


    def __init__(self, token):
        self.token = token
        self.invalidated_on = dt.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)


    @staticmethod
    def check_invalid(auth_token):

        token_exists = InvalidToken.query.filter_by(token=str(auth_token)).first()

        if token_exists:
            return True
        else:
            return False