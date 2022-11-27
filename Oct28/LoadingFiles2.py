import pyodbc


class BulkInsert:
    def __init__(self, csv_file_nm, sql_server_nm, db_nm, db_table_nm):
        # Connect to the database, perform the insert, and update the log table.
        conn = self.connectDB(sql_server_nm, db_nm)
        self.insertData(conn, csv_file_nm, db_table_nm)
        conn.close

    def connectDB(self, sql_server_nm, db_nm):
        # Connect to the server and database with Windows authentication.
        conn_string = 'DRIVER={SQL Server};Server=' + sql_server_nm + ';DATABASE=' + db_nm + ';Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
        return conn
        
    def insertData(self, conn, csv_file_nm, db_table_nm):
        # Skip the header row by specifying FIRSTROW = 2.
        qry = "BULK INSERT " + db_table_nm + " FROM '" + csv_file_nm + "' WITH (FORMAT = 'CSV', FIRSTROW = 2)"
        # Execute the query
        cursor = conn.cursor()
        cursor.execute(qry)
        conn.commit()
        cursor.close

bulk_insert = BulkInsert('C:/Users/Ezra Muir/Documents/Training-Work/Python/Oct_Learn/Oct28/load.csv', 'DESKTOP-VOT1DO6\MSSQLSERVER_NEW', 'HelloWorld', 'Employee_prof')