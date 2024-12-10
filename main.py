from database import execute_query
from view import tabel
from rich import print

def main():
    query = "SELECT * FROM detailtransaksi"
    result = execute_query(query=query)
    kolom = [("ID Detail Transaksi","right"),("ID transaksi","right"),("ID Barang","right"),("Banyak Barang","right")]
    tabel_detailTransaksi = tabel(title="Detail Transaksi",kolom=kolom,row=result)
    print (tabel_detailTransaksi)

if __name__ == "__main__":
    main()