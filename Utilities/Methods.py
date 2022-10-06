from time import time
from flask import jsonify, request, flash
import traceback
import pandas

# All endpoints must return a JSON response with status, data, message and HTTP code.
def success_response(data, code=200):
    return jsonify({
        "code": code,
        "status": True,
        "message": "success",
        "data": data,
        "endpoint": request.path,
        "timestamp": time(),
        
    })


def error_response(msg, code=400):
    data = {
        
        "code": code,
        "status": False,
        "message": str(msg),
        "data": msg,
        "timestamp": time()
        
    }
    log_error(data=data, traceback=traceback.print_exc())
    return jsonify(data), 500


def check_json(json, keys):
    for key in keys:
        if key not in json:
            return key
    return None


def log_error(data, traceback):
    pass

def display_error(msg):
    flash(msg, category='error')
    error_response(msg)
    return None
