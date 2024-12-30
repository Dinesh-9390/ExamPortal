import os
import uuid
from app import db
from sqlalchemy import func
from flask import request, make_response, jsonify
from app.models.user_mst import UserMst
from app.models.user_details import UserDetails
from app.models.user_technology import UserTechnology
from app.models.technology_mst import TechnologyMst
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
import logging


def add_user():
    # Getting the request data
    data = request.get_json()

    # Assigning the values to variables
    keys = ['first_name', 'last_name', 'email', 'mobile_number', 'aadhaar_number', 'college_name', 'roll_number', 'qualification', 'experience_type', 'experience', 'technologies']
    first_name, last_name, email, mobile_number, aadhaar_number, college_name, roll_number, qualification, experience_type, experience, technologies= (data.get(key) for key in keys)


    password = generate_password_hash(data.get('password'))

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
            password=password
        )
        db.session.add(user)

        # Flush to get user.id for foreign key reference in userDetails
        db.session.flush()

        # Create userDetails
        userDetails = UserDetails(
            user_id=user.id,
            aadhaar_number=aadhaar_number,
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
                    "status_code": 404,
                    "status_message": f"Technology '{technology_name}' not found"
                }, 404)

        # Commit all changes
        db.session.commit()

        # Return success response
        return make_response(jsonify({
            "status_code": 201,
            "status_message": "User Added Successfully'",
            "user": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "mobile_number": user.mobile_number,
                "email": user.email,
                "aadhaar_number": userDetails.aadhaar_number,
                "college_name": userDetails.college_name,
                "roll_number": userDetails.roll_number,
                "qualification": userDetails.qualification,
                "experience_type": userDetails.experience_type,
                "experience": str(userDetails.experience),
                "technologies": technologies,
            }
        }), 201)

    except Exception as e:
        # Rollback in case of any error
        db.session.rollback()
        logging.error(f"Error adding user: {str(e)}")  # Log the error for debugging

        # Return a generic error message to the user
        return make_response({
            "status_code": 500,
            "status_message": "An error occurred while processing your request."
        }, 500)


def get_all_users(page, per_page):

    try:
        offset = (page - 1) * per_page

        query = db.session.query(
            UserMst.id,
            UserMst.first_name,
            UserMst.last_name,
            UserMst.email,
            UserMst.password,
            TechnologyMst.technology_name,
            UserDetails.aadhaar_number,
            UserDetails.college_name,
            UserDetails.roll_number,
            UserDetails.qualification,
            UserDetails.experience_type,
            UserDetails.experience
        ).join(
            UserTechnology, UserTechnology.user_id == UserMst.id
        ).join(
            TechnologyMst, TechnologyMst.id == UserTechnology.technology_id
        ).join(
            UserDetails, UserDetails.user_id == UserMst.id
        ).offset(offset).limit(per_page)

        users = query.all()

        # Organize the result into a more user-friendly format
        result = []
        for user in users:
            # Check if the user already exists in the result
            user_dict = next((item for item in result if item["id"] == user.id), None)
            if user_dict:
                user_dict["technologies"].append(user.technology_name)
            else:
                result.append({
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "password": user.password,
                    "aadhaar_number": user.aadhaar_number,
                    "college_name": user.college_name,
                    "roll_number": user.roll_number,
                    "qualification": user.qualification,
                    "experience_type": user.experience_type,
                    "experience": str(user.experience),
                    "technologies": [user.technology_name]
                })

                print(result)

        return make_response({
            "status_code": 200,
            "status_message": "Data fetched successfully",
            "Data": result
        })
    except Exception as e:
        error_response = {
            "status_code": 500,
            "status_message": "An error occurred",
            "error": str(e)
        }
        return make_response(jsonify(error_response), 500)


def user_login():
    data = request.get_json()

    # Safely get email and password from the request
    email = data.get('email', 'key not found')
    password = data.get('password', 'key not found')

    # Find the user by email, ignoring case sensitivity
    user = UserMst.query.filter(func.lower(UserMst.email) == email.lower()).first()

    if user:
        try:
            # Verify the password
            if check_password_hash(user.password, password):
                # Create the JWT payload
                payload = {
                    "user_id": str(user.id),
                    "email": user.email,
                    "exp": datetime.utcnow() + timedelta(hours=24)  # Token expiration time
                }

                # Generate the JWT token
                secret = os.getenv("SECRET")
                algorithm = os.getenv("ALGORITHM")
                encoded_jwt = jwt.encode(payload, secret, algorithm=algorithm)

                # Return the response with the token
                return make_response({
                    "status_code": 200,
                    "status_message": "User Data Found",
                    "data": {
                        "email": user.email,
                        "token": encoded_jwt
                    }
                }, 200)
            else:
                return make_response({
                    "status_code": 401,
                    "status_message": "Incorrect Password"
                }, 401)

        except Exception as e:
            # Log the exception for debugging
            return make_response({
                "status_code": 500,
                "status_message": "An error occurred while processing your request."
            }, 500)

    else:
        return make_response({
            "status_code": 404,
            "status_message": "User Not Found"
        }, 404)



def get_by_user_id(user_id):
    try:
        # Check if the user_id is a valid UUID string format
        try:
            # Attempt to convert the user_id to a UUID
            uuid.UUID(user_id)  # Will raise ValueError if not a valid UUID
        except ValueError:
            return make_response({
                "status_code": 400,
                "status_message": "Invalid user ID format. It must be a valid UUID."
            }, 400)

        # Query the database for the user using the UUID, assuming it's stored as a string
        user = UserMst.query.filter(UserMst.id == user_id).first()

        if user:
            return make_response({
                "status_code": 200,
                "status_message": "User Data Found",
                "data": {
                    "user_id": user.id,
                    "email": user.email
                }
            }, 200)
        else:
            return make_response({
                "status_code": 404,
                "status_message": "User Not Found"
            }, 404)

    except Exception as e:
        # Log the error for debugging purposes (optional but recommended)
        print(f"Error occurred: {e}")
        return make_response({
            "status_code": 500,
            "status_message": "An error occurred while processing your request."
        }, 500)