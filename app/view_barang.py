from view import tabel,loading,key,tanya
from database import execute_query
from rich import print
from rich.rule import Rule
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
    clear()
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
    
    print(Rule())
    
    menu = ["No","Fungsi","Info"]
    baris_menu = [
        ('1','Edit','Edit Barang'),
        ('2','Filter','Filter Barang'),
        ('3','View All','Tanpa Limit')
    ]
    grup_menu = Group(
        (tabel("Menu",kolom=menu,baris=baris_menu)),
                      Panel(Align.center("Tekan Tombol Yang Sesuai Untuk Memilih"))
                      )
    print(Panel((grup_menu)))
    
    while True:
        pilihan = tanya(str)
        if pilihan == '1':
            loading([("Memasuki Edit",2)])
            edit()
        elif pilihan == '2':
            print("\rFilter", end="", flush=True)
        elif pilihan == '3':
            print("\rView All", end="", flush=True)
        else:
            sys.stdout.write("\rSalah Input")
            sys.stdout.flush
def edit():
    clear()
    kolom = ["No","Fungsi"]
    baris = [("1","Cari Menggunakan Kategori ?"),
             ("2","Cari Menggunakan ID ?")]
    print(Panel(Align.center(tabel("- Menu Edit -",
                                   baris=baris,
                                   kolom=kolom))))
    pilihan = tanya(str)
    
    if pilihan == "1":
        clear()
        
        kolom_kategori = ["ID","Nama"]
        data_kategori = execute_query("SELECT * FROM kategori")
        tabel_kategori = tabel("- List Kategori -",
                               kolom=kolom_kategori,
                               baris=data_kategori)
        print(Panel(tabel_kategori,
                    subtitle="Masukan angka sesuai ID Kategori untuk di-filter",
                    subtitle_align="left"))
        id_kategori = tanya(int)

        clear()
        kolom_barang = ["ID","Nama Barang"]
        data_barang = execute_query(f"SELECT idbarang,namaBarang FROM barang WHERE idKategori = {id_kategori}")
        tabel_barang = tabel("- Barang Berdasarkan Kategori -",
                                       kolom=kolom_barang,
                                       baris=data_barang)
        print(Panel(tabel_barang,
                    subtitle="Tekan angka sesuai lalu enter ID Barang untuk di-edit",
                    subtitle_align="left"))
        id_barang = tanya(int)
        
        header_tabel = ["ID",
                    "ID Kategori",
                    "ID Supplier",
                    "Nama",
                    "Harga Jual",
                    "Harga Pack"
                    ]
        data_kategori_barang = execute_query(f'SELECT * FROM barang WHERE idbarang = {id_barang}')
        tabel_kategori_barang = tabel("- Detail Barang -",
                                      kolom=header_tabel,
                                      baris=data_kategori_barang)
        print(Panel(tabel_kategori_barang,
                    subtitle="Enter untuk mulai edit",
                    subtitle_align="left"))
        input()

        clear()
        print(Panel(tabel_kategori_barang))
        print(Rule())
        kolom_supplier = ["ID","Nama Supplier"]
        data_supplier = execute_query("SELECT idsupplier,namasupplier FROM supplier")
        tabel_supplier = tabel("- List Supplier -",
                               kolom=kolom_supplier,
                               baris=data_supplier)
        print(Panel(tabel_supplier,
                    subtitle="Tekan angka sesuai lalu enter ID supplier untuk di-edit",
                    subtitle_align="left"))
        id_supplier_edit = tanya(int) # ID Supplier

        clear()
        print(Panel(tabel_kategori_barang,
                    subtitle="Masukan nama",
                    subtitle_align="left"))
        nama_barang = tanya(str) # Nama Barang

        clear()
        print(Panel(tabel_kategori_barang,
                    subtitle="Masukan harga barang (cth : 4500.00)",
                    subtitle_align="left"))
        harga_jual_barang = tanya(float) # Harga Barang
        
        clear()
        print(Panel(tabel_kategori_barang,
                    subtitle="Masukan harga pack (cth : 4500.00 bisa NULL)",
                    subtitle_align="left"))
        harga_jual_pack = tanya(float) # Harga Barang

        tabel_edit = [
            (f"{data_kategori_barang[0][0]}",)
        ]
        grub_edit = Group(Panel(tabel_kategori_barang),
                          Rule("Diubah Menjadi"),
                          Panel())
    elif pilihan == "2":
        print(Panel("Tekan angka di keyboard sesuai ID Barang"))
        print("   ╰─>")