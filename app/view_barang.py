from view import tabel,loading,tanya
from database import execute, execute_query
from rich import print
from rich.rule import Rule
from rich.align import Align
from rich.panel import Panel
from rich.console import Group
import sys,os,time

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
    
    
    menu = ["No","Fungsi","Info"]
    baris_menu = [
        ('1','Edit','Edit Barang'),
        ('2','Filter','Filter Barang'),
        ('3','View All','Tanpa Limit')
    ]
    
    grub_menu = Group(
        tabel("Barang Limit 100", kolom=header_tabel, baris=execute_query(query=query)),
        tabel("Menu",kolom=menu,baris=baris_menu),
        Panel(Align.center("Masukan Pilihan Fungsi"))
    )
    print(Panel((grub_menu),
                subtitle="╭─",
                subtitle_align="left"))
    
    while True:
        pilihan = tanya(str)
        if pilihan == '1':
            loading([("Memasuki Edit",2)])
            edit()
            break
        elif pilihan == '2':
            filter()
            break
        elif pilihan == '3':
            print("\rView All", end="", flush=True)
            break
        else:
            sys.stdout.write("\rSalah Input")
            sys.stdout.flush

def pilih_kategori():
    """Memilih kategori dari tabel kategori."""
    kolom_kategori = ["ID", "Nama"]
    data_kategori = execute_query("SELECT * FROM kategori")
    tabel_kategori = tabel("- List Kategori -", kolom=kolom_kategori, baris=data_kategori)
    print(Panel(tabel_kategori, subtitle="╭─ Masukan ID Kategori untuk di-filter", subtitle_align="left"))
    return tanya(int)

def pilih_supplier():
    """Memilih supplier dari tabel supplier."""
    kolom_supplier = ["ID", "Nama Supplier"]
    data_supplier = execute_query("SELECT idsupplier, namasupplier FROM supplier")
    tabel_supplier = tabel("- List Supplier -", kolom=kolom_supplier, baris=data_supplier)
    print(Panel(tabel_supplier, subtitle="╭─ Masukan ID Supplier untuk di-edit", subtitle_align="left"))
    return tanya(int)

def tampilkan_detail_barang(id_barang):
    """Menampilkan detail barang berdasarkan ID."""
    header_tabel = ["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"]
    data_barang = execute_query(f"SELECT * FROM barang WHERE idbarang = {id_barang}")
    tabel_barang = tabel("- Detail Barang -", kolom=header_tabel, baris=data_barang)
    print(Panel(tabel_barang, subtitle="Enter untuk mulai edit", subtitle_align="left"))
    input()
    return data_barang

def edit_barang(id_barang):
    """Melakukan proses edit barang."""
    clear()
    data_barang_lama = tampilkan_detail_barang(id_barang)

    # Pilih kategori
    clear()
    id_kategori_edit = pilih_kategori()

    # Pilih supplier
    clear()
    id_supplier_edit = pilih_supplier()

    # Masukan nama barang
    clear()
    print(Panel(data_barang_lama, subtitle="Masukan nama baru", subtitle_align="left"))
    nama_barang_edit = tanya(str)

    # Masukan harga barang
    clear()
    print(Panel(data_barang_lama, subtitle="╭─ Masukan harga barang (cth: 4500.00)", subtitle_align="left"))
    harga_jual_barang = tanya(float)

    # Masukan harga pack
    clear()
    print(Panel(data_barang_lama, subtitle="╭─ Masukan harga pack (cth: 4500.00 bisa NULL)", subtitle_align="left"))
    harga_jual_pack = tanya(float, str)

    # Konfirmasi perubahan
    clear()
    data_tabel_edit = [
        (id_barang, id_kategori_edit, id_supplier_edit, nama_barang_edit, harga_jual_barang, harga_jual_pack)
    ]
    tabel_edit = tabel("- Barang Setelah Edit -", kolom=["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"], baris=data_tabel_edit)
    print(Panel(tabel_edit, subtitle="Enter untuk melanjutkan", subtitle_align="left"))
    input()

    # Update data
    execute_query(f"""
        UPDATE barang 
        SET idkategori = {id_kategori_edit}, 
            idsupplier = {id_supplier_edit}, 
            namabarang = \"{nama_barang_edit}\", 
            hargajual = {harga_jual_barang}, 
            hargapack = {harga_jual_pack} 
        WHERE idbarang = {id_barang}
    """)
    print(Panel("Data barang berhasil diperbarui!"))
    loading([("Kembali ke menu Barang", 2)])

def edit():
    clear()
    kolom = ["No", "Fungsi"]
    baris = [
        ("1", "Cari Menggunakan Kategori"),
        ("2", "Cari Menggunakan ID"),
    ]
    print(Panel(Align.center(tabel("- Menu Edit -", baris=baris, kolom=kolom)), subtitle="╭─ Pilih Fungsi", subtitle_align="left"))
    pilihan = tanya(str)

    if pilihan == "1":
        # Cari berdasarkan kategori
        clear()
        id_kategori = pilih_kategori()
        clear()
        kolom_barang = ["ID", "Nama Barang"]
        data_barang = execute_query(f"SELECT idbarang, namaBarang FROM barang WHERE idKategori = {id_kategori}")
        tabel_barang = tabel("- Barang Berdasarkan Kategori -", kolom=kolom_barang, baris=data_barang)
        print(Panel(tabel_barang, subtitle="╭─ Masukan ID Barang untuk di-edit", subtitle_align="left"))
        id_barang = tanya(int)
        edit_barang(id_barang)

    elif pilihan == "2":
        # Cari berdasarkan ID
        print(Panel("Masukan ID Barang", subtitle="╭─ ", subtitle_align="left"))
        id_barang = tanya(int)
        edit_barang(id_barang)

def filter():
    clear()
    kolom_barang = ["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"]
    kolom_menu_filter = ["No","Filter"]
    baris_menu_filter = [
        ('1','Menggunakan Kategori'),
        ('2','Menggunakan Supplier'),
        ('3','Menggunakan Harga'),
        ('4','Menggunakan Alphabet')
    ]
    print(Panel(tabel("- Menu Filter Barang -", kolom=kolom_menu_filter, baris=baris_menu_filter),
                subtitle="╭─ Masukan Pilih Filter", subtitle_align="left"))
    Filter = tanya(int)
    
    if Filter == 1:
        clear()
        id_kategori = pilih_kategori()
        barang_kategori = execute_query(f"SELECT * FROM barang WHERE idkategori = {id_kategori}")
        print(Panel(tabel("- Barang Berdasarkan Kategori -",kolom=kolom_barang,baris=barang_kategori),
                    subtitle="Enter untuk kembali",
                    subtitle_align="left"))
        input()
        main()
        
    elif Filter == 2:
        clear()
        id_supplier = pilih_supplier()
        barang_supplier = execute_query(f"SELECT * FROM barang where idsupplier = {id_supplier}")
        print(Panel(tabel("- Barang Berdasarkan Supplier -", kolom=kolom_barang, baris=barang_supplier),
                    subtitle="Enter untuk kembali",
                    subtitle_align="left"))
        input()
        main()
        
    elif Filter == 3:
        clear()
        range_harga = execute_query("SELECT MAX(hargajual), MIN(hargajual) FROM barang")
        kolom_harga = ["Range Harga"]
        print(Panel(tabel("- Filter Harga -", kolom=kolom_harga, baris=range_harga),
                    subtitle="╭─ Masukan range harga (cth. > 4000, < 5000)", subtitle_align="left"))
        filter_harga = tanya(str)
        data_filter_harga = execute_query(f"SELECT * FROM barang WHERE hargajual {filter_harga}")
        print(Panel(tabel("- Barang Berdasarkan Harga -", kolom=kolom_barang, baris=data_filter_harga),
                    subtitle="Enter untuk kembali",
                    subtitle_align="left"))
        input()
        main()

    elif Filter == 4:
        data_nama_barang = execute_query("SELECT SUBSTRING(namabarang, 1, 1) AS Huruf FROM Barang GROUP BY Huruf ORDER BY Huruf")
        kolom_alphabet = ["Huruf"]
        while True:
            clear()
            print(Panel(tabel("- Filter Alphabet -", kolom=kolom_alphabet, baris=data_nama_barang),
                    subtitle="╭─ Masukan Alphabet yang tersedia", subtitle_align="left"))
            alphabet = tanya(str)
            
            ditemukan = False
            for ABC in data_nama_barang:
                if alphabet in ABC[0]:
                    ditemukan = True
                    break
                
            if ditemukan:
                barang_alphabet = execute_query(f"SELECT * FROM barang WHERE LOWER(namabarang) LIKE \'{alphabet}%\'")
                print(Panel(tabel(f"- Barang Berdasarkan Alphabet {alphabet}-", kolom=kolom_barang, baris=barang_alphabet),
                    subtitle="Enter untuk kembali", subtitle_align="left"))
                input()
                main()
            else:
                print("Barang tidak ada kaka")
                time.sleep(1)