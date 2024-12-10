from database import connect_db
from config import load_environ

def execute_query(query,*value):
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
