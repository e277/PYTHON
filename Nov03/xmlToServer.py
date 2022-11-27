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


    # convert the result from fetch_query to xml and write to .xml file
    tree = ET.parse('employee_3.xml')

    data2 = tree.findall('employee')

    for i, j in zip(data2, range(1, 6)):
        emp_no = i.find('Emp_no').text
        emp_name = i.find('Emp_name').text
        age = i.find('Age').text
        place = i.find('Place').text
        religion = i.find('Religion').text
        department = i.find('Department').text
        
        data = """
        INSERT INTO Employee_3 (emp_no, emp_name, age, place, religion, department) 
        VALUES(?, ?, ?, ?, ?, ?)
        """

        # creating the cursor object
        cursor = conn.cursor()
        
        # executing cursor object
        cursor.execute(data, (emp_no, emp_name, age, place, religion, department))
        conn.commit()
    
    
    print("Data inserted successfully")


if __name__ == "__main__":
    main()
    
