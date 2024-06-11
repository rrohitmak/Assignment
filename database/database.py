import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

load_dotenv()
SERVER = os.getenv("SERVER")
SERVER_USER_NAME = os.getenv("USER_NAME")
SERVER_PASSWORD = os.getenv("PASSWORD")
DATABASE_1 = "self_ship"
DATABASE_2 = "client"
conn_str_1 = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE_1};"
    f"UID={SERVER_USER_NAME};"
    f"PWD={SERVER_PASSWORD};"
    f"TrustServerCertificate=yes"
)


connection_url_1 = URL.create(
    "mssql+pyodbc", query={"odbc_connect": conn_str_1})

engine_1 = create_engine(connection_url_1, echo=True,
                         pool_size=10, max_overflow=20)
Session_1 = sessionmaker(bind=engine_1)

conn_str_2 = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE_2};"
    f"UID={SERVER_USER_NAME};"
    f"PWD={SERVER_PASSWORD};"
    f"TrustServerCertificate=yes"
)


connection_url_2 = URL.create(
    "mssql+pyodbc", query={"odbc_connect": conn_str_2})

engine_2 = create_engine(connection_url_2, echo=True,
                         pool_size=10, max_overflow=20)
Session_2 = sessionmaker(bind=engine_2)
