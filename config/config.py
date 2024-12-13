import dotenv, sys, os
from dotenv import load_dotenv

def load_environ():
    """
    Memuat konfigurasi database dari file .env dan mengembalikannya sebagai dictionary.

    Fungsi ini memuat nilai-nilai konfigurasi database seperti host, user, password, dan nama database
    dari file .env. Jika ada nilai yang kosong atau None, fungsi akan mengeluarkan pengecualian.

    Returns:
        dict: Dictionary yang berisi konfigurasi database (host, user, password, database).

    Raises:
        ValueError: Jika ada kredensial yang tidak ditemukan atau kosong di file .env.
    """
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