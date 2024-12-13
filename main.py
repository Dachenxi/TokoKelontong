from app import *
from view import tabel,loading
from rich import print

def main():
    kolom_menu = [('No'),('App'),('Status')]
    baris_menu = [(1,'View All Table','ONLINE'),
                  (2,'View Barang','On Development'),
                  (3,'View Supplier','On Development'),
                  (4,'View Transaksi','On Development')]
    main_menu = tabel(title="Main Menu App Toko Kelontong",kolom=kolom_menu,baris=baris_menu)
    print (main_menu)
    
    pilihan = {
    '1': view_all_tabel.main,
    '2': view_barang.main,
    '3': view_supplier.main,
    '4': view_transaksi.main
    }
    
    no = input("Nomor Berapa? ")
    # Panggil fungsi yang sesuai dengan nomor pilihan pengguna
    if no in pilihan:
        pilihan[no]()  # Menjalankan fungsi yang dipilih
    else:
        print("Pilihan tidak valid.")
try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    loading([
        ("Menghentikan Program",3)
    ])