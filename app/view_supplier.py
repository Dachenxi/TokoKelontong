from view import tabel, panel, tanya
from database import execute_query
from rich.console import Group
from rich.align import Align
from rich import print
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tabel_supplier(id_supplier=None):
    if id_supplier:
        data_suppler = execute_query("SELECT * FROM supplier WHERE idsupplier=%s",(id_supplier))
    else:
        data_suppler = execute_query("SELECT * FROM supplier")
    return tabel(title="- List Supplier -",kolom=["ID Supplier","Nama Supplier","Alamat","Telepon","Email"],baris=data_suppler)

def supplier():
    baris_menu = [
        ('1',"Edit", 'Edit Tabel Supplier'),
        ('2',"Filter", 'Filter Tabel Supplier'),
        ('3',"Lihat Semua", 'Lihat Semua Tabel Supplier'),
        ('4',"Kembali", 'Kembali ke Menu Utama')
    ]
    grub_menu_supplier = Group(
        panel(Align.center("- Menu Supplier -")),
        tabel_supplier(),
        tabel(title="- Menu Supplier -",kolom=["No","Menu","Status"],baris=baris_menu)
    )
    clear()
    print(panel(grub_menu_supplier,subtitle="╭─ Masukan Menu",subtitle_align="left"))
    no = tanya(str)
    if no == '1':
        edit()
    elif no == '2':
        filter()
    elif no == '3':
        Lihat_Semua()
    else:
        pass

def edit():
    menu = [
        ('1',"Tambah", 'Tambah Supplier Baru'),
        ('2',"Update", 'Update Supplier'),
        ('3',"Hapus", 'Hapus Supplier'),
        ('4',"Kembali", 'Kembali ke Menu Supplier')
    ]
    grub_edit_supplier = Group(
        panel(Align.center("- Edit Supplier -")),
        tabel_supplier(),
        tabel(title="- Edit Supplier -",kolom=["No","Menu","Status"],baris=menu)
    )
    clear()
    print(panel(grub_edit_supplier,subtitle="╭─ Masukan Menu",subtitle_align="left"))
    no = tanya(str)
    if no == '1':
        while True:
            clear()
            grub_tambah_supplier = Group(
                panel(Align.center("- Tambah Supplier -")),
                panel(Align.center("- Konfirmasi -"))
            )
            print(panel(grub_tambah_supplier,subtitle="╭─ 1 Untuk kembali, Kosongi untuk lanjut",subtitle_align="left"))
            konfirmasi = tanya(str)
            if konfirmasi:
                break
            else:
                tambah_supplier()
        edit()
    if no == '2':
        while True:
            clear()
            grub_update_supplier = Group(
                panel(Align.center("- Update Supplier -")),
                panel(Align.center("- Konfirmasi -"))
            )
            print(panel(grub_update_supplier,subtitle="╭─ 1 Untuk kembali, Kosongi untuk lanjut",subtitle_align="left"))
            konfirmasi = tanya(str)
            if konfirmasi:
                break
            else:
                update_supplier()
        edit()
    if no == '3':
        while True:
            clear()
            grub_hapus_supplier = Group(
                panel(Align.center("- Hapus Supplier -")),
                panel(Align.center("- Konfirmasi -"))
            )
            print(panel(grub_hapus_supplier,subtitle="╭─ 1 Untuk kembali, Kosongi untuk lanjut",subtitle_align="left"))
            konfirmasi = tanya(str)
            if konfirmasi:
                break
            else:
                hapus_supplier()
        edit()
    else:
        supplier()

def data_supplier_edit(idsupplier=None):
    clear()
    if idsupplier:
        tabel_supplier_edit = tabel_supplier(idsupplier)
    else:
        tabel_supplier_edit = tabel_supplier()

    grub_tambah_supplier = Group(
        tabel_supplier_edit,
        panel(Align.center("- Masukan Nama Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─",subtitle_align="left"))
    namasupplier = tanya(str)

    clear()
    grub_tambah_supplier = Group(
        tabel_supplier_edit,
        panel(Align.center("- Masukan Alamat Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─",subtitle_align="left"))
    alamat = tanya(str)

    clear()
    grub_tambah_supplier = Group(
        tabel_supplier_edit,
        panel(Align.center("- Masukan Telepon Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─",subtitle_align="left"))
    notelepon = tanya(str)

    clear()
    grub_tambah_supplier = Group(
        tabel_supplier_edit,
        panel(Align.center("- Masukan Email Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─ Boleh NULL",subtitle_align="left"))
    email = tanya(str)

    return (namasupplier,alamat,notelepon,email)

def tambah_supplier():

    clear()
    kolom_data_tambah = ["NamaSupplier","Alamat","Telepon","Email"]
    data_tambah = data_supplier_edit()
    grub_tambah_supplier = Group(
        tabel(title="- Supplier Ditambahkan -",kolom=kolom_data_tambah,baris=[data_tambah]),
        panel(Align.center("- Konfirmasi Tambah Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─ 1 Untuk ulangi, Kosongi untuk lanjut",subtitle_align="left"))
    konfirmasi = tanya(str)

    if konfirmasi:
        tambah_supplier()
    else:
        query = "INSERT INTO supplier (namasupplier,Alamat,notelepon,Email) VALUES (%s,%s,%s,%s)"
        execute_query(query,*data_tambah)

    grub_tambah_supplier = Group(
        tabel_supplier(),
        panel(Align.center("- Berhasil Menambahkan Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─ 1 Untuk tambah lagi, Kosongi untuk kembali ke-edit",subtitle_align="left"))
    lagi = tanya(str)
    if lagi:
        tambah_supplier()

def update_supplier():
    clear()
    grub_update_supplier = Group(
        tabel_supplier(),
        panel(Align.center("- Masukan ID Supplier -"))
    )

    print(panel(grub_update_supplier,subtitle="╭─ Masukan ID Supplier yang ingin di edit",subtitle_align="left"))
    idsupplier = tanya(str)

    print(panel(tabel_supplier(idsupplier),subtitle="╭─ 1 Untuk ulangi, Kosongi untuk lanjut",subtitle_align="left"))
    konfirmasi = tanya(str)

    if konfirmasi:
        update_supplier()

    data_update = data_supplier_edit(idsupplier)
    grub_tambah_supplier = Group(
        tabel_supplier(),
        tabel(title="- Supplier Diupdate -",kolom=["NamaSupplier","Alamat","Telepon","Email"],baris=[data_update]),
        panel(Align.center("- Konfirmasi Update Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─ 1 Untuk ulangi, Kosongi untuk lanjut",subtitle_align="left"))
    konfirmasi = tanya(str)
    if konfirmasi:
        update_supplier()
    else:
        query = f"UPDATE supplier SET namasupplier=%s,Alamat=%s,notelepon=%s,Email=%s WHERE idsupplier={idsupplier}"
        execute_query(query,*data_update)
    grub_tambah_supplier = Group(
        tabel_supplier(),
        panel(Align.center("- Berhasil Menambahkan Supplier -"))
    )
    print(panel(grub_tambah_supplier,subtitle="╭─ 1 Untuk update lagi, Kosongi untuk kembali ke-edit",subtitle_align="left"))
    lagi = tanya(str)
    if lagi:
        update_supplier()

def hapus_supplier():
    clear()
    grub_hapus_supplier = Group(
        tabel_supplier(),
        panel(Align.center("- Masukan ID Supplier -"))
    )

    print(panel(grub_hapus_supplier,subtitle="╭─ Masukan ID Supplier yang ingin di hapus",subtitle_align="left"))
    idsupplier = tanya(str)
    if not idsupplier:
        edit()

    print(panel(tabel_supplier(idsupplier),subtitle="╭─ 1 Untuk ulangi, Kosongi untuk lanjut",subtitle_align="left"))
    konfirmasi = tanya(str)

    if konfirmasi:
        hapus_supplier()
    else:
        query = f"DELETE FROM supplier WHERE idsupplier={idsupplier}"
        execute_query(query)
    grup_lagi_supplier = Group(
        tabel_supplier(),
        panel(Align.center("- Berhasil Menghapus Supplier -"))
    )
    print(panel(grup_lagi_supplier,subtitle="╭─ 1 Untuk hapus lagi, Kosongi untuk kembali ke-edit",subtitle_align="left"))
    lagi = tanya(str)
    if lagi:
        hapus_supplier()


def filter():
    pass

def Lihat_Semua():
    pass
