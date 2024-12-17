from rich import print
import sys

def tanya(*tipe):
    """
    Meminta input dari pengguna dan memvalidasi tipe data yang diizinkan.
    
    Parameters:
        *tipe: Satu atau lebih tipe data yang diizinkan (e.g., int, float, str).
    
    Returns:
        Input pengguna yang sudah divalidasi sesuai tipe yang diizinkan.
    
    Contoh:
    >>> hasil = tanya(int, float)
    >>> print("Hasil input:", hasil)
    """
    while True:
        pilihan = input("   ╰─> ")
        for tipe_data in tipe:
            try:
                return tipe_data(pilihan)
            except ValueError:
                continue
        print("Value tidak valid. Masukkan nilai dengan tipe yang sesuai:", tipe)