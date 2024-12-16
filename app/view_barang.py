from view import tabel,loading
from database import execute_query
from rich import print

def main():
    loading([
        ("Mengambil Data Barang", 0.5)
    ])
    query = "SELECT * FROM barang"
    header_tabel = ["ID",
                    "ID Kategori",
                    "ID Supplier",
                    "Nama",
                    "Harga Jual",
                    "Harga Pack"
                    ]
    print(
        execute_query(query=query)
    )
    print(tabel("Barang",
                kolom=header_tabel,
                baris=execute_query(query=query)
                )
          )
    