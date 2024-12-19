from rich import print
from rich.console import Group
from rich.columns import Columns
from rich.align import Align
from datetime import datetime
from app import menu
from view import panel
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

jam = datetime.now()
now = datetime.strftime(jam,"%d/%m/%Y %H:%M:%S")
kolom_title = Columns([
    Align.left("Interface Untuk Database Toko Kelontong"),
    Align.right(f"{now}")
    ],expand=True)

kolom_ending = Columns([
    Align.left("Terima kasih sudah menggunakan program ini"),
    Align.right(f"{now}")
    ],expand=True)
changelog = "Version 1.0"
grub_main_menu = Group(panel(kolom_title),
                       panel(changelog),
                       fit=False)
grub_ending = Group(panel(kolom_ending))

try:
    clear()
    print(panel(grub_main_menu,
                subtitle="Enter Untuk Melanjutkan Ke Program", subtitle_align="left"))
    input()
    menu()
except KeyboardInterrupt:
    print()
    print(panel(grub_ending))