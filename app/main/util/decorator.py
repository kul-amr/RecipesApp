from functools import wraps
from flask import request

from app.main.service.auth_service import Auth



def token_required(f):

    @wraps(f)
    def decorated(*args,**kwargs):

        resp, status = Auth.get_loggedin_user(request)
        token = resp.get('data')

        if not token:
            return resp, status

        return f(*args,**kwargs)

    return decorated


