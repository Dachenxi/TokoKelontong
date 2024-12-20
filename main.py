try:
    import rich, mysql.connector
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "rich", "mysql-connector-python"])

from rich import print
from rich.console import Group
from rich.columns import Columns
from rich.align import Align
from datetime import datetime
from app import menu
from view import panel
from database import create_database
from database import connect_db
from config import load_environ
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

jam = datetime.now()
now = datetime.strftime(jam,"%d/%m/%Y %H:%M:%S")
ascii_art = r''' .-') _                .-. .-')
(  OO) )               \  ( OO )
/     '._  .-'),-----. ,--. ,--.  .-'),-----.
|'--...__)( OO'  .-.  '|  .'   / ( OO'  .-.  '
'--.  .--'/   |  | |  ||      /, /   |  | |  |
   |  |   \_) |  |\|  ||     ' _)\_) |  |\|  |
   |  |     \ |  | |  ||  .   \    \ |  | |  |
   |  |      `'  '-'  '|  |\   \    `'  '-'  '
   `--'        `-----' `--' '--'      `-----'
'''

kolom_title = Columns([
    Align.left("Interface Untuk Database Toko Kelontong"),
    Align.right(f"{now}")
    ],expand=True)

kolom_ending = Columns([
    Align.left("Terima kasih sudah menggunakan program ini"),
    Align.right(f"{now}")
    ],expand=True)
changelog = """Version 1.0
> Initial Release
> 1. View All Table
> 2. View Barang
> 3. View Supplier

> Jangan berharap berjalan dengan lancar karena masih dalam tahap pengembangan
> Menemukan bug? Silahkan hubungi developer
> Terima kasih
"""
grub_main_menu = Group(panel(kolom_title),
                       panel(Align.center(ascii_art)),
                       panel(changelog),
                       fit=False)
grub_ending = Group(panel(kolom_ending))

config = load_environ()

db, cursor = connect_db(config)

try:
    cursor.execute("SELECT * FROM barang")
except:
    create_database()

try:
    clear()
    print(panel(grub_main_menu,
                subtitle="Enter Untuk Melanjutkan Ke Program", subtitle_align="left"))
    input()
    menu()
except KeyboardInterrupt:
    print()
    print(panel(grub_ending))