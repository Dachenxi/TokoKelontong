from view import tabel,tanya, panel
from rich import print
from .view_barang import barang
from .view_supplier import supplier
from .view_all_tabel import view_all
from .view_transaksi import transaksi
import os

def clear():
     os.system("cls" if os.name == "nt" else "clear")

def menu():
    kolom_menu = [('No'),('App'),('Status')]
    baris_menu = [(1,'View All Table','ONLINE'),
                  (2,'View Barang','On Development'),
                  (3,'View Supplier','On Development'),
                  (4,'View Transaksi','On Development')]
    main_menu = tabel(title="Main Menu App Toko Kelontong",
                      kolom=kolom_menu,
                      baris=baris_menu)

    while True:
        clear()
        print (panel(main_menu,
                     subtitle="╭─ Masukan App", subtitle_align="left"))
        no = tanya(str)
        if no == '1':
            view_all()
        elif no == '2':
            barang()
        elif no == '3':
            supplier()
        elif no == '4':
            transaksi()