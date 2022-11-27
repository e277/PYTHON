import pandas as pd
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

# Perform the following operations:

# 1. Write a program that opens the CSV file, reads its records one-by-one, and calls a SQL
#    INSERT statement to insert the rows into a database table.
def quest1():
    # See Oct28
    pass


# 2. Generate a CSV file with 10,000 records of fabricated data from the free Online Data
#    Generator.
#    a. The file is &lt;FILE&gt;.csv .
#    b. It contains the columns ID, Job Title, Email Address, and FirstName LastName.
#    c. A Python program will execute a SQL Server BULK INSERT statement to load data
#    from the file into a table.
def quest2():
    # create table
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS Load_csv_tb;")
        cursor.execute("""
        CREATE TABLE Load_csv_tb (
            ID INT,
            Job_Title VARCHAR(255),
            Email_Address VARCHAR(255),
            First_Name VARCHAR(255),
            Last_Name VARCHAR(255)
        )
        """)
        print("Table created successfully!!!")
        conn.commit()
    except Exception as e:
        print(e)

    def insertOnlineRecs():
        # insert csv records
        try:
            query = "BULK INSERT Load_csv_tb FROM 'C:/Users/Ezra Muir/Documents/Training-Work/Python/Oct_Learn/Oct31/employee.csv' WITH (FORMAT='csv', FIRSTROW=2)"
            cursor.execute(query)
            print("Bulk insert success!")
            conn.commit()
            cursor.close
        except Exception as e:
            print(e)
    
    insertOnlineRecs()


# 3. Write a program that opens the SQL server file, reads its records one-by-one, and calls a
#    function to to insert the rows into a CSV file.
def quest3():
    try:
        query3 = pd.read_sql_query('''
        SELECT * FROM Employee_prof
        ''',
        conn)
        df = pd.DataFrame(query3)
        df.to_csv(r'C:/Users/Ezra Muir/Documents/Training-Work/Python/Oct_Learn/Oct31/Output.csv', index=False)
    except Exception as e:
        print(e)


def main():
    # quest2()
    quest3()

if __name__ == "__main__":
    main()