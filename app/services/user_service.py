from app import db
from sqlalchemy import func
from flask import request, make_response, jsonify
from app.models.user_mst import UserMst
from app.models.user_details import UserDetails
from app.models.user_technology import UserTechnology
from app.models.technology_mst import TechnologyMst
import logging  # For error logging


def add_user():
    # Getting the request data
    data = request.get_json()

    # Assigning the values to variables
    keys = ['first_name', 'last_name', 'email', 'mobile_number', 'adhaar_number', 'college_name', 'roll_number', 'qualification', 'experience_type', 'experience', 'technologies']
    first_name, last_name, email, mobile_number, adhaar_number, college_name, roll_number, qualification, experience_type, experience, technologies = (data.get(key) for key in keys)

    # Check if mobile number already exists
    existing_user_mobile = UserMst.query.filter_by(mobile_number=mobile_number).first()
    if existing_user_mobile:
        return make_response({
            "status_code": 409,
            "status_message": "Mobile Number Already Exists"
        }, 409)

    # Check if email already exists (case-insensitive) and handle None values safely
    if email:
        existing_user_email = UserMst.query.filter(func.lower(UserMst.email) == email.lower()).first()
        if existing_user_email:
            return make_response({
                "status_code": 409,
                "status_message": "Email Already Exists"
            }, 409)

    # Ensure technologies is not None or an empty list
    if not technologies:
        return make_response({
            "status_code": 400,
            "status_message": "Technologies cannot be empty"
        }, 400)

    try:
        # Create and add user
        user = UserMst(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
        )
        db.session.add(user)

        # Flush to get user.id for foreign key reference in userDetails
        db.session.flush()

        # Create userDetails
        userDetails = UserDetails(
            user_id=user.id,
            adhaar_number=adhaar_number,
            college_name=college_name,
            roll_number=roll_number,
            qualification=qualification,
            experience_type=experience_type,
            experience=experience,
        )
        db.session.add(userDetails)

        # Add technologies to user
        for technology_name in technologies:
            technology = TechnologyMst.query.filter(func.lower(TechnologyMst.technology_name) == technology_name.lower()).first()

            if technology:
                userTechnology = UserTechnology(
                    user_id=user.id,
                    technology_id=technology.id
                )
                db.session.add(userTechnology)
            else:
                return make_response({
                    "status_code": 400,
                    "status_message": f"Technology '{technology_name}' not found"
                }, 400)

        # Commit all changes
        db.session.commit()

        # Return success response
        return make_response(jsonify({
            "status_code": 200,
            "status_message": "User Added Successfully'",
            "user": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "mobile_number": user.mobile_number,
                "email": user.email,
                "adhaar_number": userDetails.adhaar_number,
                "college_name": userDetails.college_name,
                "roll_number": userDetails.roll_number,
                "qualification": userDetails.qualification,
                "experience_type": userDetails.experience_type,
                "experience": str(userDetails.experience),
                "technologies": technologies,
            }
        }), 200)

    except Exception as e:
        # Rollback in case of any error
        db.session.rollback()
        logging.error(f"Error adding user: {str(e)}")  # Log the error for debugging

        # Return a generic error message to the user
        return make_response({
            "status_code": 500,
            "status_message": "An error occurred while processing your request."
        }, 500)