from flask import Blueprint, request
from app.services.user_service import add_user, get_all_users, user_login, get_by_user_id
from app.utils.decorators import token_required

# Creating a Blueprint for the users
user_bp=Blueprint('users', __name__)


@user_bp.route('/add-user', methods=['POST'])
def create_user():
    user = add_user()
    return user


@user_bp.route('/get-all-users', methods=['GET'])
def get_users():

    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', type=int)

    users = get_all_users(page, per_page)
    return users

@user_bp.route('/login', methods=['POST'])
def login():
    login_status = user_login()
    return login_status

@user_bp.route('/get-by-user-id', methods=['GET'])
@token_required
def get_by_id():

    user_id = request.args.get('user_id', type=str)
    user = get_by_user_id(user_id)
    return user