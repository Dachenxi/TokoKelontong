import mysql.connector
from mysql.connector import Error

def connect_db(config):
    """
    Menghubungkan ke database MySQL menggunakan konfigurasi yang diberikan.

    Args:
        config (dict): Sebuah dictionary yang berisi konfigurasi untuk koneksi ke database,
                       yang meliputi:
                       - host: Alamat server database.
                       - user: Nama pengguna untuk koneksi.
                       - password: Kata sandi untuk pengguna.
                       - database: Nama database yang ingin diakses.

    Returns:
        tuple: Mengembalikan objek koneksi (`db`) dan objek cursor (`cursor`) jika berhasil
               menghubungkan ke database.

    Raises:
        Error: Jika terjadi kegagalan saat menghubungkan ke database, akan melemparkan
               exception dengan pesan kesalahan.
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