from .. import db, flask_bcrypt
import datetime as dt
import jwt
from app.main.model.invalidToken import InvalidToken
from ..config import key


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String(255), unique = True, nullable=False)
    user_id = db.Column(db.String(50),unique=True)
    created_date = db.Column(db.DateTime,nullable=False)
    username = db.Column(db.String(50),unique=True)
    password_hash = db.Column(db.String(100))


    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self,password):
        return flask_bcrypt.check_password_hash(self.password_hash,password)


    def __repr__(self):
        return "<User '{}'>".format(self.username)


    def encode_auth_token(self, user_id):

        try:
            payload = {
                # 'exp':dt.datetime.utcnow()+dt.timedelta(days=1),
                #        'created':dt.datetime.utcnow(),
                       'sub':user_id}

            return jwt.encode(payload,key,algorithm='HS256')
        except Exception as e:
            return e


    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token,key)
            is_token_invalid = InvalidToken.check_invalid(auth_token)

            if is_token_invalid:
                return 'token invalid. Please login again'
            else:
                return payload['sub']

        except jwt.ExpiredSignatureError:
            return 'signature expired. Please login again'
        except jwt.InvalidTokenError:
            return 'token invalid. Please login again'
