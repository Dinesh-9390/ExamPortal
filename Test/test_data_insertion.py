import pandas as pd
from app import db
from app.models.technology_mst import TechnologyMst
from sqlalchemy import text
import os

def data_insert():
    raw_data_path = 'C:\\Users\\Dinesh Kumar Reddy\\OneDrive - Sparity INC\\Desktop\\ExamPortal\\Test\\data\\technologies.csv'

    df = pd.read_csv(raw_data_path)
    technologies = df['Technologies'].tolist()

    try:

        db.session.execute(text( 'TRUNCATE TABLE public.technology_mst CASCADE'))
        db.session.commit()

        for tech in technologies:
            if tech:
                technology = TechnologyMst(
                    technology_name=tech
                )
                db.session.add(technology)
                db.session.commit()
        return 'Technologies Inserted'
    except Exception as e:
        db.session.rollback()
        print(e)
        return 'Error in Technologies insertion'