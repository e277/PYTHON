import pyodbc

try:
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=DESKTOP-VOT1DO6\MSSQLSERVER_NEW;'
        'Database=HelloWorld;'
        'Trusted_Connection=yes;'
    )
    print("Connection Established")

except Exception as e:
    print("Connection Failed")


def insertCsvData():
    cursor = conn.cursor()
    # path_to_csv = "C:/Users/Ezra Muir/Documents/Training-Work/Python/Oct_Learn/Oct28/load.csv"
    query = "BULK INSERT Employee_prof FROM 'C:/Users/Ezra Muir/Documents/Training-Work/Python/Oct_Learn/Oct28/load.csv' WITH (FORMAT='csv', FIRSTROW=2)"
    cursor.execute(query)
    print("Bulk insert success!")
    conn.commit()
    cursor.close
    

def main():
    insertCsvData()

if __name__ == "__main__":
    main()