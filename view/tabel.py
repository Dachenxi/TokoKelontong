import rich
from rich import box
from rich.table import Table

def tabel(title:str,kolom:list, row:list):
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
    for columns_list in kolom:
        columns = columns_list[0]
        justify = columns_list[1] if len(columns) > 1 else "left"
        tabel.add_column(columns.capitalize(), justify=justify)
    
    for row in row:
        tabel.add_row(*[str(value) for value in row])
    
    return tabel