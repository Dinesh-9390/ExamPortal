import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuring the database url to the flask-migrate
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONN')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controller.user_controller import user_bp
    from app.controller.role_controller import role_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(role_bp, url_prefix='/api/roles')


    with ((app.app_context())):
     from app.models import user_mst,user_details, technology_mst, user_technology, exams, sections, sub_sections, exam_section, user_exam_map, questions_mst, role_mst, user_role_map

     """
     Inserting the test data into master tables
     """
     # from Test.test_data_insertion import data_insert
     # result = data_insert()
     # print(result)

    return app