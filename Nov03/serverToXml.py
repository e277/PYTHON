import pyodbc
import urllib
from xml.dom.minidom import parse, parseString


cnxn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-VOT1DO6\MSSQLSERVER_NEW;'
    'Database=HelloWorld;'
    'Trusted_Connection=yes;'
)

idPerson = 2

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Employee_3')

for row in cursor.fetchall():
    print(row)

    # insert row into xml file
    doc = parse("data.xml")
    root = doc.documentElement
    newElement = doc.createElement("Employee")
    root.appendChild(newElement)

    # create Emp_no element
    idElement = doc.createElement("Emp_no")
    idText = doc.createTextNode(str(row[0]))
    idElement.appendChild(idText)
    newElement.appendChild(idElement)

    # create Emp_name element
    nameElement = doc.createElement("Emp_name")
    nameText = doc.createTextNode(str(row[1]))
    nameElement.appendChild(nameText)
    newElement.appendChild(nameElement)

    # create Age element
    ageElement = doc.createElement("Age")
    ageText = doc.createTextNode(str(row[2]))
    ageElement.appendChild(ageText)
    newElement.appendChild(ageElement)

    # create Place element
    placeElement = doc.createElement("Place")
    placeText = doc.createTextNode(str(row[3]))
    placeElement.appendChild(placeText)
    newElement.appendChild(placeElement)

    # create Religion element
    religionElement = doc.createElement("Religion")
    religionText = doc.createTextNode(str(row[4]))
    religionElement.appendChild(religionText)
    newElement.appendChild(religionElement)

    # create Department element
    departmentElement = doc.createElement("Department")
    departmentText = doc.createTextNode(str(row[5]))
    departmentElement.appendChild(departmentText)
    newElement.appendChild(departmentElement)

    # after writing to xml file, remove the empty lines in the xml file
    with open("data.xml", "w") as f:
        f.write(doc.toprettyxml())
    
    # remove empty lines
    with open("data.xml", "r") as f:
        lines = f.readlines()
    with open("data.xml", "w") as f:
        for line in lines:
            if line.strip():
                f.write(line)

cnxn.close()

