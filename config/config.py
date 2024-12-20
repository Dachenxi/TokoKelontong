import dotenv, sys, os
from dotenv import load_dotenv
from view import panel, tanya
from rich import print

def clear():
    os.system("cls" if os.name == "nt" else "clear")
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
        clear()
        print(panel("Masukan Database Host ",subtitle="╭─",subtitle_align="left"))
        dbhost = tanya(str)
        print(panel("Masukan Username",subtitle="╭─",subtitle_align="left"))
        username = tanya(str)
        print(panel("Masukan Password",subtitle="╭─",subtitle_align="left"))
        password = tanya(str)

        config_folder = "config"
        config_file = ".env"
        if not os.path.exists(config_folder):
            os.makedirs(config_folder)
        with open(f"{config_folder}/{config_file}","w") as f:
            f.write(f"DB_HOST={dbhost}\n")
            f.write(f"DB_USER={username}\n")
            f.write(f"DB_PASSWORD={password}\n")
            f.write("DB_DATABASE=tokokelontong\n")

        load_environ()
    else:
        return config