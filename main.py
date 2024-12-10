from database import execute_query

def main():
    query = "SELECT * FROM detailtransaksi"
    result = execute_query(query=query)
    print (result)

if __name__ == "__main__":
    main()