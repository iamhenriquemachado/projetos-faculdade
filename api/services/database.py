from dotenv import load_dotenv
import os
import pyodbc
from models.message import MSG


load_dotenv()

DRIVER = '{ODBC Driver 17 for SQL Server}'
DB_SERVER = os.getenv("DB_SERVER")
DB_SCHEMA = os.getenv("DATABASE_SCHEMA")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


connection_string = f'DRIVER={DRIVER};SERVER={DB_SERVER};DATABASE={DB_SCHEMA};UID={DB_USER};PWD={DB_PASSWORD}'

def get_connection():
    return pyodbc.connect(connection_string, timeout=5)

def execute_query(query, params=None):
    return True

def checkSqlServerConnection():
    try:
        with pyodbc.connect(connection_string, timeout=5) as conn:

            cursor = conn.cursor()
            cursor.execute("SELECT TOP 1 1 FROM [Contas]")
            row = cursor.fetchall()

            if row and row[0][0] == 1:
                print(MSG.DATABASE_CONNECTED)
                return True
            else:
                print(MSG.DATABASE_QUERY_FAILED)
                return False
            
    except pyodbc.Error as exception:
        print(f"{MSG.DATABASE_CONNECTION_FAILED}")
        print(f"Details: {exception}")
        return False
    except Exception as e:
        print(f"{MSG.ERROR_DEFAULT}")
        print(f"Details: {e}")
        return False

            


