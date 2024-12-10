from database import connect_db
from config import load_environ

def main():
    # Muat konfigurasi dari file .env
    config = load_environ()

    # Koneksi ke database
    conn = connect_db(config)
    if conn:
        print("Koneksi berhasil!")
        # Lakukan operasi lain, misalnya query
        conn.close()

if __name__ == "__main__":
    main()