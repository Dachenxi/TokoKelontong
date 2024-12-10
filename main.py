import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

def cek_kredensial():
    # Muat variabel dari file .env
    load_dotenv()

    # Ambil kredensial dari environment variables
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")

    # Cek jika ada kredensial yang hilang
    if None in [host, user, password, database]:
        print("Beberapa kredensial database tidak ditemukan. Pastikan file .env sudah diatur dengan benar.")

    else:
        try:
            # Menghubungkan ke database
            db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            if db.is_connected():
                print("Koneksi Terhubung.")

        except Error as e:
            print(f"Gagal menghubungkan ke database: {e}")
        finally:
            # Menutup koneksi jika terbuka
            if db.is_connected():
                db.close()
                print("Koneksi ditutup.")