import os
import pyodbc
from dotenv import load_dotenv
import logging

load_dotenv()

try:
    DRIVER = '{ODBC Driver 17 for SQL Server}'
    DB_SERVER = os.environ["DB_SERVER"]
    DB_SCHEMA = os.environ["DATABASE_SCHEMA"]
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]

    connection_string = f'DRIVER={DRIVER};SERVER={DB_SERVER};DATABASE={DB_SCHEMA};UID={DB_USER};PWD={DB_PASSWORD}'
except KeyError as e:
    logging.error(f"Erro: Variável de ambiente não encontrada - {e}")
    raise SystemExit(f"Variável de ambiente {e} não configurada.")

def get_connection():
    try:
        return pyodbc.connect(connection_string, timeout=5)
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        logging.error(f"Erro de conexão com o banco de dados: {sqlstate}")
        raise

def fetch_one(query: str, params: tuple = None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params if params else [])
                return cursor.fetchone()
    except pyodbc.Error as e:
        logging.error(f"Erro ao executar fetch_one: {e}")
        return None

def fetch_all(query: str, params: tuple = None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params if params else [])
                return cursor.fetchall()
    except pyodbc.Error as e:
        logging.error(f"Erro ao executar fetch_all: {e}")
        return []

def execute_commit(query: str, params: tuple = None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params if params else [])
                conn.commit()
                return cursor.rowcount 
    except pyodbc.Error as e:
        logging.error(f"Erro ao executar execute_commit: {e}")
        return None