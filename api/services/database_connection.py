from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

DRIVER = '{ODBC Driver 17 for SQL Server}'
DB_SERVER = os.getenv("DB_SERVER")
DB_SCHEMA = os.getenv("DATABASE_SCHEMA")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

connection_string = f'DRIVER={DRIVER};SERVER={DB_SERVER};DATABASE={DB_SCHEMA};UID={DB_USER};PWD={DB_PASSWORD}'

