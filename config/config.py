import dotenv, sys, os
from dotenv import load_dotenv

def load_environ():
    load_dotenv()  # Muat file .env

    config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE")
    }

    if "" in config.values() or None in config.values():
        raise ValueError("Beberapa kredensial database tidak ditemukan. Pastikan file .env sudah diatur dengan benar.")
    else:
        return config