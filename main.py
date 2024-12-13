from app import *
from view import tabel
from rich import print

def main():
    kolom_menu = [('No'),('App'),('Status')]
    baris_menu = [(1,'View All Table','On Development'),
                  (2,'View Barang','On Development'),
                  (3,'View Supplier','On Development'),
                  (4,'View Transaksi','On Development')]
    main_menu = tabel(title="Main Menu App Toko Kelontong",kolom=kolom_menu,baris=baris_menu)
    print (main_menu)

if __name__ == "__main__":
    view_all_tabel.main()