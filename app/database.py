import os

import pandas as pd
import pyodbc
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    driver = os.getenv("DB_DRIVER")

    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    return pyodbc.connect(connection_string)


def execute_query(query):
    connection = get_connection()

    try:
        df = pd.read_sql(query, connection)
        return df
    finally:
        connection.close()