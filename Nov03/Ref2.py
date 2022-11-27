import pyodbc
import urllib
import xml.etree.ElementTree as ET


def main():
    # connect python to sql server
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

    query = """
    DECLARE @Employee TABLE (Emp_no INT, Emp_name NVARCHAR(255), Age INT, Place NVARCHAR(255), Religion NVARCHAR(255), Department NVARCHAR(255));
    INSERT INTO @Employee (Emp_no, Emp_name, Age, Place, Religion, Department) VALUES
    ('C:/Users/Ezra Muir/Documents/Training-Work/Python/Nov_Learn/Nov03/employee_3.xml' , 2),   

    SELECT @Employee
        
    DECLARE @hdoc INT
        
    EXEC sp_xml_preparedocument @hdoc OUTPUT, @emp
    SELECT *
    FROM OPENXML (@hdoc, 'C:/Users/Ezra Muir/Documents/Training-Work/Python/Nov_Learn/Nov03/employee_3.xml' , 2)
    WITH (
        Emp_no INT,
        Emp_name VARCHAR(255),
        Age INT,
        Place VARCHAR(255),
        Religion VARCHAR(255),
        Department VARCHAR(255)
    )

    EXEC sp_xml_removedocument @hdoc
    """

    cursor = conn.cursor()
    if cursor.execute(query):
        print("Query executed")
        conn.commit()


if __name__ == "__main__":
    main()
