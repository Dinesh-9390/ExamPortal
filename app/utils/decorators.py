import functools
import os
import jwt
from flask import request, make_response

# Secret key for encoding and decoding JWT (it should match the one used to encode tokens)
SECRET_KEY = os.getenv("SECRET")


# Decorator function to check if the JWT token is present and valid
def token_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the token from the Authorization header
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]  # "Bearer <token>"

        if not token:
            return make_response({
                "status_code": 403,
                "status_message": "Token is missing!"}, 403)

        try:
            # Decode the token using the secret key
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            # Add the decoded data (usually user information) to the request context
            request.user_data = data
        except jwt.ExpiredSignatureError:
            return make_response({
                "status_code": 401,
                "status_message": "Token is expired!"}, 401)
        except jwt.InvalidTokenError:
            return make_response({
                "status_code": 401,
                "status_message": "Invalid Token!"}, 401)

        return f(*args, **kwargs)

    return decorated_function
