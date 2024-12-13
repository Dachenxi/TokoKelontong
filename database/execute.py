from database import connect_db
from config import load_environ

def execute_query(query,*value):
    """
    Mengeksekusi query SQL pada database MySQL.

    Args:
        query (str): Query SQL yang ingin dijalankan, bisa berupa perintah SELECT atau non-SELECT.
        *value: Nilai-nilai yang akan digunakan dalam query, biasanya digunakan untuk menggantikan placeholder
                dalam query (misalnya, untuk parameterized query).

    Returns:
        list of tuple: Mengembalikan hasil query dalam bentuk list of tuple jika query adalah SELECT.
        None: Untuk query selain SELECT, fungsi ini hanya mengembalikan None setelah melakukan commit.

    Raises:
        Error: Jika ada kesalahan saat menghubungkan ke database atau mengeksekusi query.
    """
    config = load_environ() # load config Environ
    
    db, cursor = connect_db(config) # Konek db menggunakan config
    
    cursor.execute(query, value) # value adalah tuple
    
    if query.strip().upper().startswith("SELECT"):
        # Untuk query SELECT, kita hanya mengembalikan hasilnya
        result = cursor.fetchall()  # Mengambil semua hasil
        cursor.close()
        db.close()
        return result # result adalah list of tuple (tuplelist)
    else:
        # Untuk query selain SELECT, lakukan commit
        db.commit()
        cursor.close()
        db.close()