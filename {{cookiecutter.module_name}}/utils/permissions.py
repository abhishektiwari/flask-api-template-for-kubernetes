"""
Util functions to check permission
"""
from functools import wraps
from flask import jsonify
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_claims
)
from {{cookiecutter.module_name}}.apis.options import ERR_UNAUTH

def permission_required(*allowed_roles):
    """Check required JWT scope present"""
    def decorator(fn): #pylint: disable-msg=C0103
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            for role in allowed_roles:
                if role in claims['scopes']:
                    return fn(*args, **kwargs)
            return jsonify({"msg": ERR_UNAUTH}), 403
        return wrapper
    return decorator

def company_match(fn): #pylint: disable-msg=C0103
    """Match company with scope"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        cuuid = kwargs['cuuid']
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if cuuid not in claims['companies']:
            return jsonify({"msg": ERR_UNAUTH}), 403
        else:
            return fn(*args, **kwargs)
    return wrapper
