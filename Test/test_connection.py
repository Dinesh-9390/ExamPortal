import os
import pyodbc
from sqlalchemy import text
from sqlalchemy import create_engine

# Your connection string
Database_Con = "mssql+pyodbc://sa:1234@DINESH-KUMAR-RE/Examportal?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
# Create an engine
engine = create_engine(Database_Con)

def test_connection():
    try:
        # Connect to the database
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print(result)
            print("Connection successful!" if result.fetchone() else "Connection failed!")
    except Exception as e:
        print(f"Connection failed: {e}")


test_connection()