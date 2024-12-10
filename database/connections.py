import mysql.connector
from mysql.connector import Error

def connect_db(config):
    try:
        db = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        if db.is_connected():
            return db
        
    except Error as e:
        raise Error(f"Gagal menghubungkan ke database | {e}")
        