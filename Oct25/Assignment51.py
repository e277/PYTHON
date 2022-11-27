import pyodbc

def checkConnection():
    try:
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=DESKTOP-VOT1DO6\MSSQLSERVER_NEW;'
            'Database=BikeStores;'
            'Trusted_Connection=yes;'
        )
        print("Connection Established")
        return conn
    except Exception as e:
        print("Connection Failed")

def proStockDuplicates():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        # query3 = """
        # SELECT *
        # FROM 
        # production.products
            
        # """

        query3 = """
        SELECT *
        FROM 
            (SELECT product_name, 
                ROW_NUMBER() OVER(PARTITION BY product_name ORDER BY product_name) Duplicates
            FROM production.products
            ) AS D
        WHERE Duplicates > 1;
        """
        if cursor.execute(query3):
            print("\nAll Duplicates")
            for r in cursor.fetchall():
                print(r)


# Calling Functions
def main():
    # checkConnection()
    proStockDuplicates()

if __name__ == "__main__":
    main()