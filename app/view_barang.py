import os,time
from view import tabel,tanya, panel
from database import execute_query
from rich import print
from rich.align import Align
from rich.console import Group
from rich.columns import Columns

def clear():
     os.system("cls" if os.name == "nt" else "clear")

def barang():
    clear()
    query = "SELECT * FROM barang LIMIT 20"
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
        ('3','View All','Tanpa Limit'),
        ('4','Kembali ke menu utama','')
    ]

    grub_menu = Group(
        tabel("- Barang Limit 20 -", kolom=header_tabel, baris=execute_query(query=query)),
        tabel("Menu",kolom=menu,baris=baris_menu),
        panel(Align.center("Masukan Pilihan Fungsi"))
    )
    print(panel((grub_menu),
                subtitle="╭─",
                subtitle_align="left"))

    pilihan = tanya(str)
    if pilihan == '1':
        edit()
    elif pilihan == '2':
        filter()
    elif pilihan == '3':
        print("\rView All", end="", flush=True)
    else:
        pass

def tabel_kategori():
    """Memilih kategori dari tabel kategori."""
    kolom_kategori = ["ID", "Nama"]
    data_kategori = execute_query("SELECT * FROM kategori")
    tabel_kategori = tabel("- List Kategori -", kolom=kolom_kategori, baris=data_kategori)
    return tabel_kategori

def tabel_supplier():
    """Memilih supplier dari tabel supplier."""
    kolom_supplier = ["ID", "Nama Supplier"]
    data_supplier = execute_query("SELECT idsupplier, namasupplier FROM supplier")
    tabel_supplier = tabel("- List Supplier -", kolom=kolom_supplier, baris=data_supplier)
    return tabel_supplier

def tampilkan_detail_barang(id_barang):
    """Menampilkan detail barang berdasarkan ID."""
    header_tabel = ["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"]
    data_barang = execute_query(f"SELECT * FROM barang WHERE idbarang = {id_barang}")
    tabel_barang = tabel("- Detail Barang -", kolom=header_tabel, baris=data_barang)
    return data_barang, tabel_barang

def update_tabel(a, data):
    tambah_data = a[0] + (data,)
    a[0] = tambah_data

def edit_barang(id_barang):
    data_tabel_edit = [
        (id_barang,)
    ]
    """Melakukan proses edit barang."""
    clear()
    data_barang, tabel_barang = tampilkan_detail_barang(id_barang)
    print(panel(Group(tabel_barang),
                subtitle="Enter untuk mulai edit", subtitle_align="left"))
    input()

    # Pilih kategori
    clear()
    tabel_kategori_edit = tabel_kategori()
    print(panel(Group(tabel_barang,tabel_kategori_edit),
                subtitle="╭─ Masukan ID-Kategori untuk di-edit", subtitle_align="left"))
    id_kategori_edit = tanya(int)

    # Pilih supplier
    clear()
    tabel_supplier_edit = tabel_supplier()
    print(panel(Group(tabel_barang, tabel_supplier_edit),
                subtitle="╭─ Masukan ID-Supplier untuk di-edit", subtitle_align="left"))
    id_supplier_edit = tanya(int)

    # Masukan nama barang
    clear()
    print(panel(Group(tabel_barang),
                subtitle="╭─ Masukan nama baru", subtitle_align="left"))
    nama_barang_non_kapital = tanya(str)
    nama_barang_edit = nama_barang_non_kapital.title()

    # Masukan harga barang
    clear()
    print(panel(Group(tabel_barang),
                subtitle="╭─ Masukan harga barang (cth: 4500.00)", subtitle_align="left"))
    harga_jual_barang = tanya(float)

    # Masukan harga pack
    clear()
    print(panel(Group(tabel_barang),
                subtitle="╭─ Masukan harga pack (cth: 4500.00 bisa NULL)", subtitle_align="left"))
    harga_jual_pack = tanya(float, str)

    # Konfirmasi perubahan
    clear()

    data_tabel_edit = [
        (id_barang, id_kategori_edit, id_supplier_edit, nama_barang_edit, harga_jual_barang, harga_jual_pack)
    ]
    tabel_barang_sebelum = tabel("- Barang Sebelum Di-Edit -",kolom=["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"], baris=data_barang)
    tabel_edit = tabel("- Barang Setelah Edit -", kolom=["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"], baris=data_tabel_edit)
    print(panel(Group(tabel_barang_sebelum,tabel_edit), subtitle="Enter untuk melanjutkan", subtitle_align="left"))
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
    print(panel("Data barang berhasil diperbarui!, Enter untuk melanjutkan"))
    input()

def edit():
    clear()
    kolom = ["No", "Fungsi"]
    baris = [
        ("1", "Cari Menggunakan Kategori"),
        ("2", "Cari Menggunakan ID"),
    ]
    print(panel(tabel("- Menu Edit -", baris=baris, kolom=kolom), subtitle="╭─ Pilih Fungsi", subtitle_align="left"))
    pilihan = tanya(str)

    if pilihan == "1":
        clear()
        tabel_kategori_filter = tabel_kategori()
        print(panel(tabel_kategori_filter,
                    subtitle="╭─ Masukan ID-Kategori untuk di-filter", subtitle_align="left"))
        id_kategori = tanya(int)
        clear()
        kolom_barang = ["ID", "Nama Barang"]
        data_barang = execute_query(f"SELECT idbarang, namaBarang FROM barang WHERE idKategori = {id_kategori}")
        tabel_barang = tabel("- Barang Berdasarkan Kategori -", kolom=kolom_barang, baris=data_barang)
        print(panel(tabel_barang, subtitle="╭─ Masukan ID Barang untuk di-edit", subtitle_align="left"))
        id_barang = tanya(int)
        edit_barang(id_barang)

    elif pilihan == "2":
        data_id_barang = execute_query("SELECT idbarang FROM barang ORDER BY idbarang ASC")
        kolom_id_barang = Columns([panel(Align.center(str(value[0]))) for value in data_id_barang])
        while True:
            clear()
            print(panel(kolom_id_barang, subtitle="╭─ Masukan ID Barang", subtitle_align="left"))
            id_barang = tanya(int)
            data_barang_id, a = tampilkan_detail_barang(id_barang=id_barang)
            tabel_barang_sebelum = tabel("- Barang Sebelum Di-Edit -",kolom=["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"], baris=data_barang_id)

            if id_barang:
                clear()
                print(panel(tabel_barang_sebelum,
                            subtitle="╭─ Ya untuk lanjut, kosongi untuk pilih id lagi", subtitle_align="left"))
                benar = tanya(str)
                if benar:
                    edit_barang(id_barang)
            else: pass


def filter():
    kolom_barang = ["ID", "ID Kategori", "ID Supplier", "Nama", "Harga Jual", "Harga Pack"]
    kolom_menu_filter = ["No","Filter"]
    baris_menu_filter = [
        ('1','Menggunakan Kategori'),
        ('2','Menggunakan Supplier'),
        ('3','Menggunakan Harga'),
        ('4','Menggunakan Alphabet'),
        ('5','Menggunakan Harga Pack'),
        ('6','Kembali Ke Menu Utama')
    ]

    while True:
        clear()
        print(panel(tabel("- Menu Filter Barang -", kolom=kolom_menu_filter, baris=baris_menu_filter),
                    subtitle="╭─ Masukan Pilih Filter", subtitle_align="left"))
        Filter = tanya(int)

        if Filter == 1:
            while True:
                clear()
                print(panel(tabel_kategori(),
                            subtitle="Masukan ID-Kategori untuk Di-Filter, kosongi untuk kembali", subtitle_align="left"))
                id_kategori = tanya(int, str)
                if id_kategori:
                    barang_kategori = execute_query(f"SELECT * FROM barang WHERE idkategori = {id_kategori}")
                    print(panel(tabel("- Barang Berdasarkan Kategori -",kolom=kolom_barang,baris=barang_kategori),
                                subtitle="Enter untuk kembali",
                                subtitle_align="left"))
                    input()
                else:
                    break

        elif Filter == 2:
            while True:
                clear()
                print(panel(tabel_supplier(),
                            subtitle="Masukan ID-Supplier untuk Di-edit", subtitle_align="left"))
                id_supplier = tanya(int, str)
                if id_supplier:
                    barang_supplier = execute_query(f"SELECT * FROM barang where idsupplier = {id_supplier}")
                    print(panel(tabel("- Barang Berdasarkan Supplier -", kolom=kolom_barang, baris=barang_supplier),
                                subtitle="Enter untuk kembali",
                                subtitle_align="left"))
                    input()
                else:
                    break

        elif Filter == 3:
            range_harga = execute_query("SELECT MAX(hargajual), MIN(hargajual) FROM barang")
            kolom_harga = ["MAX","MIN"]
            while True:
                clear()
                print(panel(tabel("- Filter Harga -", kolom=kolom_harga, baris=range_harga),
                            subtitle="╭─ Masukan range harga (cth. > 4000, < 5000), Kosongi untuk kembali", subtitle_align="left"))
                filter_harga = tanya(str)
                if filter_harga:
                    data_filter_harga = execute_query(f"SELECT * FROM barang WHERE hargajual {filter_harga}")
                    print(panel(tabel("- Barang Berdasarkan Harga -", kolom=kolom_barang, baris=data_filter_harga),
                                subtitle="Enter untuk kembali",
                                subtitle_align="left"))
                    input()
                else:
                    break

        elif Filter == 4:
            data_nama_barang = execute_query("SELECT SUBSTRING(namabarang, 1, 1) AS Huruf FROM Barang GROUP BY Huruf ORDER BY Huruf")
            kolom_alphabet = ["Huruf"]
            while True:
                clear()
                print(panel(tabel("- Filter Alphabet -", kolom=kolom_alphabet, baris=data_nama_barang),
                        subtitle="╭─ Masukan Alphabet yang tersedia, Kosongi untuk kembali", subtitle_align="left"))
                alphabet = tanya(str)
                if alphabet:
                    ditemukan = False
                    for ABC in data_nama_barang:
                        if alphabet in ABC[0]:
                            ditemukan = True
                            break

                    if ditemukan:
                        barang_alphabet = execute_query(f"SELECT * FROM barang WHERE LOWER(namabarang) LIKE \'{alphabet}%\'")
                        print(panel(tabel(f"- Barang Berdasarkan Alphabet {alphabet}-", kolom=kolom_barang, baris=barang_alphabet),
                            subtitle="Enter untuk kembali", subtitle_align="left"))
                        input()
                    else:
                        print(panel(Align.center("Barang tidak ada kaka"),border_style="bright red"))
                        time.sleep(1)
                else:
                    break


        elif Filter == 5:
            data_null = execute_query("SELECT COUNT(*), COUNT(hargaPack), COUNT(*) - COUNT(hargaPack) FROM barang")
            kolom_null = ["Total Barang","Memiliki Harga Pack","Tidak Memiliki Harga Pack"]
            baris_pack_filter = [
                ('1','Yang memiliki Harga pack'),
                ('2','Yang tidak memiliki Harga pack')
            ]
            grup_pack =Group(
                tabel("- Filter Harga Pack -", kolom=kolom_null, baris=data_null),
                tabel("- Pilihan Filter -", kolom=['no','Filter'],baris=baris_pack_filter)
            )
            while True:
                clear()

                print(panel(grup_pack,
                            subtitle="╭─ Masukan No Fungsi, Kosongi untuk kembali", subtitle_align="left"))
                filter_pack = tanya(int, str)
                if filter_pack:
                    if filter_pack == 1:
                        clear()
                        barang_null = execute_query("SELECT * FROM barang WHERE hargapack IS NOT NULL")
                        print(panel(tabel("- Barang Tanpa Harga Pack -", kolom=kolom_barang, baris=barang_null),
                            subtitle='Enter Untuk Kembali',subtitle_align='left'))
                        input()

                    if filter_pack == 2:
                        clear()
                        barang_null = execute_query("SELECT * FROM barang WHERE hargapack IS NULL")
                        print(panel(tabel("- Barang Tanpa Harga Pack -", kolom=kolom_barang, baris=barang_null),
                            subtitle='Enter Untuk Kembali',subtitle_align='left'))
                        input()
                else:
                    break

        elif Filter == 6:
            barang()