from flask import request, make_response
from app import db
from app.models.role_mst import RoleMst
from sqlalchemy.sql import func


def create_role():

    data = request.get_json()
    role_type = data.get('role_type')

    try:
        role = RoleMst.query.filter(func.lower(RoleMst.role_type) == role_type.lower()).first()

        if role:
            return make_response({
                "status_code": 409,
                "status_message": "Role Already Exists"
            }, 409)
        else:

            role = RoleMst(
                role_type=role_type
            )

            db.session.add(role)
            db.session.commit()

            return make_response({
                "status_code": 201,
                "status_message": "Role Created Successfully",
                "data": role.to_dict()
            }, 201)

    except Exception as e:
        return make_response({
            "status_code": 500,
            "status_message": "An error occurred while processing your request.",
            "error": str(e)
        }, 500)

