from flask import Blueprint
from app.services.user_service import add_user
from flask import make_response, jsonify

# Creating a Blueprint for the users
user_bp= Blueprint('users', __name__)


@user_bp.route('/add-user', methods=['POST'])
def create_user():
    user = add_user()
    return user