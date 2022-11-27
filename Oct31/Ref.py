import csv
import datetime
import os
import pyodbc
import shutil

# File path and name.
# filePath = 'c:\\demo\\'
filePath = 'C:/Users/Ezra Muir/Documents/Training-Work/Python/Oct_Learn/Oct31/'
fileName = 'employee_prof.csv'

# Check if the file path exists.
if os.path.exists(filePath):
    try:
        # Connect to database.
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=DESKTOP-VOT1DO6\MSSQLSERVER_NEW;'
            'Database=HelloWorld;'
            'Trusted_Connection=yes;'
        )
    except pyodbc.Error as e:
        # Confirm unsuccessful connection and stop program execution.
        print("Database connection unsuccessful.")
        quit()

    # Cursor to execute query.
    cursor = conn.cursor()

    # SQL to select data from the person table.
    sqlSelect = """
    SELECT Emp_no, Emp_name, Age, Religion, Department 
    FROM Employee_3 
    ORDER BY Emp_no
    """

    try:
        # Execute query.
        cursor.execute(sqlSelect)

        # Fetch the data returned.
        results = cursor.fetchall()

        # Extract the table headers.
        headers = [i[0] for i in cursor.description]

        # Open CSV file for writing.
        with open(filePath + fileName, 'w') as csvFile:
            # Create CSV writer.   
            writer = csv.writer(csvFile, delimiter=',', lineterminator='\r', quoting=csv.QUOTE_ALL, escapechar='\\')

            # Add the headers and data to the CSV file.
            writer.writerow(headers)
            writer.writerows(results)

        # Today's date.
        today = datetime.datetime.now().date()

        # Construct the backup file name.
        fileNameBackup = fileName[0:-4] + "_" + today.strftime("%w") + "_" + today.strftime("%A").lower() + ".csv"

        # Check if the backup file does not exist, or if it does, check that
        # today's date is different from the last modified date.
        if not(os.path.isfile(filePath + fileNameBackup)) or \
           (os.path.isfile(filePath + fileNameBackup) and \
           today != datetime.date.fromtimestamp(os.stat(filePath + fileNameBackup).st_ctime)):

            # Copy the CSV export.
            shutil.copyfile(filePath + fileName, filePath + fileNameBackup)

        # Message stating export successful.
        print("Data export successful.")

    except pyodbc.Error as e:
        # Message stating export unsuccessful.
        print("Data export unsuccessful.")
        quit()

    finally:
        # Close database connection.
        conn.close()

else:
    # Message stating file path does not exist.
    print("File path does not exist.")