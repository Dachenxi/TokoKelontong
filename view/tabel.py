from rich.table import Table
from rich.align import Align
import random

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
    one_dark_colors = [
    "#C678DD",  # Purple - Keywords
    "#61AFEF",  # Blue - Function Names
    "#E06C75",  # Red/Pink - Variables & Constants
    "#98C379",  # Green - Strings
    "#D19A66",  # Orange - Numbers
    "#56B6C2",  # Cyan - Operators & Symbols
    "#E5C07B",  # Yellow - Constants
    "#528BFF",  # Brighter Blue - Focused or Active Items
    "#BE5046",  # Dark Red - Error Highlights
    "#C18401",  # Gold - Subtle Accent
    ]

    border_color = random.choice(one_dark_colors)
    tabel = Table(title=title, expand=True, border_style=border_color)

    for idx, columns in enumerate(kolom):
        # Periksa tipe data di baris pertama untuk menentukan justify
        if baris and not isinstance(baris[0][idx], str):  # Jika bukan string
            justify = "right"
        else:  # Jika string
            justify = "left"
        tabel.add_column(Align.center(columns.capitalize()), justify=justify)

    for row in baris:
        tabel.add_row(*[str(value) for value in row])

    return tabel