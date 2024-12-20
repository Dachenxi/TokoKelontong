import os
from view import tabel, tanya, panel
from rich import print
from .connections import connect_db

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def test_connection():
    try:
        connect_db()
    except:
        config()

def config():
    clear()
    print(panel("Masukan Database Host ",subtitle="╭─",subtitle_align="left"))
    dbhost = tanya(str)
    print(panel("Masukan Username",subtitle="╭─",subtitle_align="left"))
    username = tanya(str)
    print(panel("Masukan Password",subtitle="╭─",subtitle_align="left"))
    password = tanya(str)
    return dbhost, username, password

def create_config(host,username, password):
    config_folder = "config"
    config_file = ".env"
    if not os.path.exists(config_folder):
        os.makedirs(config_folder)
    with open(f"{config_folder}/{config_file}","w") as f:
        f.write(f"DB_HOST={host}\n")
        f.write(f"DB_USER={username}\n")
        f.write(f"DB_PASSWORD={password}\n")
        f.write("DB_DATABASE=tokokelontong\n")

def create_database():
    from database import execute_query
    execute_query("SOURCE MySQL/database.sql")
