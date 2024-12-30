import pandas as pd
from app import db
from app.models.technology_mst import TechnologyMst
from app.models.user_mst import UserMst
from app.models.user_details import UserDetails
from app.models.user_technology import UserTechnology
from sqlalchemy import text, func
from werkzeug.security import generate_password_hash

def data_insert():
    raw_data_technologies_path = 'C:\\Users\\Dinesh Kumar Reddy\\OneDrive - Sparity INC\\Desktop\\ExamPortal\\Test\\data\\technologies.csv'
    raw_data_test_users_path = r'C:\Users\Dinesh Kumar Reddy\OneDrive - Sparity INC\Desktop\\ExamPortal\Test\data\test_users.csv'

    # Reading Technologies into a DataFrame
    tech_df = pd.read_csv(raw_data_technologies_path)
    technologies = tech_df['Technologies'].tolist()

    # Reading Test Users into a DataFrame
    test_users_df = pd.read_csv(raw_data_test_users_path)

    try:
        # Truncate existing tables to start fresh
        db.session.execute(text('TRUNCATE TABLE public.technology_mst CASCADE'))
        db.session.execute(text('TRUNCATE TABLE public.user_mst CASCADE'))
        db.session.commit()

        # Insert technologies into the database
        for tech in technologies:
            if tech:
                technology = TechnologyMst(technology_name=tech)
                db.session.add(technology)
        db.session.commit()

        # Insert test users directly into the database
        for index, row in test_users_df.iterrows():
            # Insert the user into the user_mst table
            user = UserMst(
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                mobile_number=row['mobile_number'],
                password=generate_password_hash(row['password'])
            )
            db.session.add(user)
            db.session.commit()

            # Insert the user details into user_details table
            user_details = UserDetails(
                user_id=user.id,
                aadhaar_number=row['adhaar_number'],
                college_name=row['college_name'],
                roll_number=row['roll_number'],
                qualification=row['qualification'],
                experience_type=row['experience_type'],
                experience=row['experience']
            )
            db.session.add(user_details)
            db.session.commit()

            # Insert technologies into user_technology table
            user_technologies = row['technologies'].split(',')  # assuming it's a comma-separated list
            for tech_name in user_technologies:
                technology = TechnologyMst.query.filter(func.lower(TechnologyMst.technology_name) == tech_name.lower()).first()
                if technology:
                    user_technology = UserTechnology(
                        user_id=user.id,
                        technology_id=technology.id
                    )
                    db.session.add(user_technology)
                else:
                    print(f"Technology '{tech_name}' not found.")
            db.session.commit()

        return 'Data Inserted Successfully'

    except Exception as e:
        db.session.rollback()
        print(e)
        return 'Error in Data Insertion'
