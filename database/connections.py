import mysql.connector
from mysql.connector import Error

def connect_db(config):
    """Koneksi Ke Database

    Args:
        config (dict): Dict config .env

    Raises:
        Error: Gagal menghubungkan ke databases

    Returns:
        function: db, cursor
    """
    try:
        db = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        if db.is_connected():
            cursor = db.cursor()
            return db, cursor
        
    except Error as e:
        raise Error(f"Gagal menghubungkan ke database | {e}")