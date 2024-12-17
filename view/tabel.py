from rich import box
from rich.table import Table
from rich.align import Align

def tabel(title:str,kolom:list, baris:list):
    """
    Membuat tabel Rich dengan kolom yang bisa memiliki justifikasi berbeda.
    
    Parameters:
    - columns: List of tuples (col_name, justify=None) -> contoh: [("ID", "right"), ("Name",)]
               Jika justify tidak diberikan, default adalah "left".
    - rows: List of tuples -> columns_list untuk tabel, contoh: [(1, "Apple", 1.5), (2, "Banana", 0.8)]
    
    Returns:
    - Rich Table object
    """
    tabel = Table(title=title)
    for idx, columns in enumerate(kolom):
        if baris and isinstance(baris[0][idx], (int,float)):
            justify = "right"
        else:
            justify = "left"
        tabel.add_column(Align.center(columns.capitalize()), justify=justify)
    for row in baris:
        tabel.add_row(*[str(value) for value in row])
    return tabel