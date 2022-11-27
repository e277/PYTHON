import pandas as pd
import pyodbc


# data = pd.read_csv('C:/Users/Ezra Muir/Documents/Training-Work/Python/Oct_Learn/Oct28/load.csv')
# df = pd.DataFrame(data)
# print(df)

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


def insertData():
    cursor = conn.cursor()
    
    with open("load.txt") as infile:
        for line in infile:
            data = line.split(",")
            query = ("INSERT INTO Employee_prof(Emp_no,Emp_name,Department,Designation,Salary) "
                    "VALUES (?, ?, ?, ?, ?)")
            cursor.execute(query, data[0], data[1], data[2], data[3], data[4])
            conn.commit()
    print("Data in file with .txt extension insertted successfully!!!")


def main():
    insertData()

if __name__ == "__main__":
    main()