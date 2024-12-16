from rich import print,box
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from database import execute_query,connect_db
from config import load_environ
from view import tabel,loading
from time import sleep

db, cursor = connect_db(load_environ())

def nama_kolom(namaTabel):
    query = f"DESCRIBE {namaTabel}"
    cursor.execute(query)
    result = [row[0] for row in cursor.fetchall()]
    return result

def generate_tabel(nama:str):
    query = f"SELECT * FROM {nama} "
    result = execute_query(query=query)
    return tabel(title=f"View Table {nama}",kolom=nama_kolom(f"{nama}"),
                  baris=result)

def main():
    loading([
        ("Mengambil Data dari server", 1)
    ])
    grub_barang = Panel(Align.center(Columns([
                Align.center(generate_tabel("barang")),
                Align.center(generate_tabel("kategori"))
            ])))
    print(grub_barang)
    sleep(0.5)
    grub_transaksi = Panel(Align.center(Columns([
                Align.center(generate_tabel("transaksi")),
                Align.center(generate_tabel("detailtransaksi"))
            ])))
    print(grub_transaksi)
    sleep(0.5)
    grub_supplier = Panel(Align.center(Columns([
                Align.center(generate_tabel("supplier")),
                Align.center(generate_tabel("transaksisupplier"))
            ])))
    print(grub_supplier)
    sleep(0.5)
    