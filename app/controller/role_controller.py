from flask import Blueprint, request
from app.services.role_service import create_role

# Creating a Blueprint for the roles
role_bp = Blueprint('roles',__name__)

@role_bp.route('/add-role', methods=['POST'])
def add_role():

    role = create_role()
    return role