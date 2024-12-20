import os,time
from view import tabel, tanya, panel
from database import execute_query
from rich import print
from rich.align import Align
from rich.console import Group
from rich.columns import Columns



def clear():
    os.system("cls" if os.name == "nt" else "clear")

def transaksi():
    baris_menu = [
        ('1','Detail Transaksi','Melihat Detail Transaksi'),
        ('2', 'Filter Transaksi', 'Filter Transaksi'),
        ('3', 'Kembali', 'Kembali ke Menu Utama')
    ]
    grub_menu_transaksi = Group(
        panel(Align.center("- Menu Transaksi -")),
        tabel_transaksi(),
        tabel(title="- Menu Transaksi -",kolom=["No","Menu","Fungsi"],baris=baris_menu)
    )
    clear()
    print(panel(grub_menu_transaksi,subtitle="╭─ Masukan Menu",subtitle_align="left"))
    no = tanya(str)
    if no == '1':
        detail_transaksi()
    elif no == '2':
        filter_transaksi()
    else:
        pass

def lihat_detail(idtransaksi):
    data_transaksi = execute_query("SELECT namabarang, banyakbarang FROM detailtransaksi INNER JOIN barang USING (idbarang) WHERE idtransaksi=%s",(idtransaksi))
    return data_transaksi

def tabel_transaksi(idtransaksi=None):
    if idtransaksi:
        data_transaksi = execute_query("SELECT * FROM transaksi WHERE idtransaksi=%s",(idtransaksi))
    else:
        data_transaksi = execute_query("SELECT * FROM transaksi")
    return tabel(title="- List Transaksi -",kolom=["ID Transaksi","Waktu Transaksi","Total bayar"],baris=data_transaksi)

def detail_transaksi():
    grup_detail_transaksi = Group(
        panel(Align.center("- Detail Transaksi -")),
        tabel_transaksi(),
        panel(Align.center("Masukan ID Transaksi"))
    )
    clear()
    print(panel(grup_detail_transaksi,subtitle="╭─",subtitle_align="left"))
    idtransaksi = tanya(str)
    if idtransaksi:
        data_detail_transaksi = tabel(title="- Detail Transaksi -",kolom=["Nama Barang","Banyak Barang"],baris=lihat_detail(idtransaksi))
        grub_detail = Group(
            panel(Align.center("- Detail Transaksi -")),
            tabel_transaksi(idtransaksi),
            data_detail_transaksi
        )
        clear()
        print(panel(grub_detail,subtitle="╭─ 1 Untuk lagi, Enter untuk kembali",subtitle_align="left"))
        kembali = tanya(str)
        if kembali:
            detail_transaksi()
        else:
            transaksi()
    else:
        detail_transaksi()

def filter_transaksi():
    baris_filter = [
        ('1','Filter Tanggal','Filter Transaksi Berdasarkan Tanggal'),
        ('2','Filter Total Bayar','Filter Transaksi Berdasarkan Total Bayar'),
        ('3','Kembali','Kembali ke Menu Transaksi')
    ]
    tabel_filter = tabel(title="- Filter Transaksi -",kolom=["No","Filter","Fungsi"],baris=baris_filter)
    grub_filter = Group(
        panel(Align.center("- Filter Transaksi -")),
        tabel_filter,
        panel(Align.center("Masukan Filter"))
    )
    clear()
    print(panel(grub_filter,subtitle="╭─",subtitle_align="left"))
    no = tanya(str)
    if no == '1':
        filter_tanggal()
    elif no == '2':
        filter_total()
    else:
        transaksi()

def filter_tanggal():
    list_tanggal = execute_query("SELECT DISTINCT DATE(waktutransaksi) FROM transaksi")
    baris_tanggal = [(idx+1, tanggal[0]) for idx, tanggal in enumerate(list_tanggal)]
    tabel_tanggal = tabel(title="- Filter Tanggal -",kolom=["No","Tanggal"],baris=baris_tanggal)
    grub_tanggal = Group(
        panel(Align.center("- Filter Tanggal -")),
        tabel_tanggal,
        panel(Align.center("Masukan No Tanggal"))
    )
    clear()
    print(panel(grub_tanggal,subtitle="╭─",subtitle_align="left"))
    no = tanya(str)
    if no:
        tanggal = list_tanggal[int(no)-1][0]
        data_transaksi = execute_query("SELECT * FROM transaksi WHERE DATE(waktutransaksi)=%s",(tanggal))
        tabel_data = tabel(title="- Filter Tanggal -",kolom=["ID Transaksi","Waktu Transaksi","Total Bayar"],baris=data_transaksi)
        grub_data = Group(
            panel(Align.center("- Filter Tanggal -")),
            tabel_data
        )
        clear()
        print(panel(grub_data,subtitle="╭─ 1 untuk ulangi, Enter untuk kembali",subtitle_align="left"))
        kembali = tanya(str)
        if kembali:
            filter_tanggal()
        else:
            filter_transaksi()
    else:
        filter_tanggal()

def filter_total():
    rentang_harga = execute_query("SELECT MIN(totalbayar), MAX(totalbayar) FROM transaksi")
    tabel_harga = tabel(title="- Filter Total Bayar -",kolom=["Min","Max"],baris=[rentang_harga[0]])
    grub_harga = Group(
        panel(Align.center("- Filter Total Bayar -")),
        tabel_harga,
    )
    clear()
    print(panel(grub_harga,subtitle="╭─ Masukan Rentang Harga cth. > 15000, < 100000",subtitle_align="left"))
    harga = tanya(str)
    if harga:
        data_transaksi = execute_query(f"SELECT * FROM transaksi WHERE totalbayar {harga}")
        tabel_data = tabel(title="- Filter Total Bayar -",kolom=["ID Transaksi","Waktu Transaksi","Total Bayar"],baris=data_transaksi)
        grub_data = Group(
            panel(Align.center("- Filter Total Bayar -")),
            tabel_data
        )
        clear()
        print(panel(grub_data,subtitle="╭─ 1 untuk ulangi, Enter untuk kembali",subtitle_align="left"))
        kembali = tanya(str)
        if kembali:
            filter_total()
        else:
            filter_transaksi()
    else:
        filter_total()