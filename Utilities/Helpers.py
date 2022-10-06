import re
import unidecode
import json


from functools import wraps

from flask_jwt_extended import create_access_token, set_access_cookies, set_refresh_cookies, create_refresh_token
from flask_jwt_extended.view_decorators import _decode_jwt_from_request
from datetime import timedelta

from .Methods import success_response

from flask import redirect

'''
Some handy helper methods and to enhance SOC and dry
'''

def auth_response(username):
    resp = success_response({'login': True})
    expires = timedelta(days=5)
    # Create the tokens we will be sending back to the user
    access_token = create_access_token(identity=username, expires_delta=expires)
    refresh_token = create_refresh_token(identity=username)

    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp


def redirect_if_jwt_invalid(view_function):
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        # attempt to grab the jwt from request
        try:
            jwt_data = _decode_jwt_from_request(request_type='access')
        except:
            jwt_data = None

        jwt_data_json = json.dumps(jwt_data)

        # if the grab worked and the identity key is in the dict then proceed
        if jwt_data_json and 'identity' in jwt_data_json:
            return view_function(*args, **kwargs)
        else:
            return redirect('login', code=302)

    return wrapper


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)

