from app import *
from view import tabel,loading,tanya
from rich import print
from rich.panel import Panel
import os

def clear():
     os.system("cls" if os.name == "nt" else "clear")

def main():
    kolom_menu = [('No'),('App'),('Status')]
    baris_menu = [(1,'View All Table','ONLINE'),
                  (2,'View Barang','On Development'),
                  (3,'View Supplier','On Development'),
                  (4,'View Transaksi','On Development')]
    main_menu = tabel(title="Main Menu App Toko Kelontong",
                      kolom=kolom_menu,
                      baris=baris_menu)

    clear()
    print (Panel(main_menu,
                 subtitle="╭─ Masukan App", subtitle_align="left"))

    no = tanya(str)
    if no == '1':
        view_all_tabel.main()
    elif no == '2':
        view_barang.barang()
    elif no == '3':
        view_supplier.main()
    elif no == '4':
        view_transaksi.main()
if __name__ == "__main__":
    main()