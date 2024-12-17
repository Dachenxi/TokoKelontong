from view import tabel,loading,key
from database import execute_query
from rich import print
from rich.align import Align
from rich.panel import Panel
from rich.console import Group
import sys,os

def clear():
     os.system("cls" if os.name == "nt" else "clear")

def main():
    loading([
        ("Mengambil Data Barang", 0.5)
    ])
    
    query = "SELECT * FROM barang LIMIT 100"
    header_tabel = ["ID",
                    "ID Kategori",
                    "ID Supplier",
                    "Nama",
                    "Harga Jual",
                    "Harga Pack"
                    ]
    print(Panel(Align.center(tabel("Barang Limit 100",
                kolom=header_tabel,
                baris=execute_query(query=query)
                ))))
    
    menu = ["No","Fungsi","Info"]
    baris_menu = [
        ('1','Edit','Edit Barang'),
        ('2','Filter','Filter Barang'),
        ('3','View All','Tanpa Limit')
    ]
    grup_menu = Group(Align.center(tabel("Menu",kolom=menu,baris=baris_menu)),
                      Panel("Tekan Tombol Yang Sesuai Untuk Memilih"))
    print(Panel(Align.center(grup_menu)))
    
    while True:
        pilihan = key()
        if pilihan == '1':
            print("\rEdit", end="", flush=True)
        elif pilihan == '2':
            print("\rFilter", end="", flush=True)
        elif pilihan == '3':
            print("\rView All", end="", flush=True)
        else:
            sys.stdout.write("\rPilihan Tidak Valid")
            sys.stdout.flush()

def edit():
    clear()
    loading([
        ("Memasuki Menu Edit")
    ])