import pyodbc


# Connect Python and SQL server and perform the following

# a. Connection established – True
# Print => connection established

# else
# Print => connection failed

# b. Create a table for employee : Emp_no
# and Emp_name

# c. Insert elements :

# Emp_no | Emp_name
# 101 | Bolt
# 102 | Subash


def checkConnection():
    try:
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=DESKTOP-VOT1DO6\MSSQLSERVER_NEW;'
            'Database=HelloWorld;'
            'Trusted_Connection=yes;'
        )
        print("Connection Established")
        return conn
    except Exception as e:
        print("Connection Failed")

def createTable():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS Employee_3")

        table = "Emp_no INT, \nEmp_name VARCHAR(255)"

        if cursor.execute("CREATE TABLE Employee_3 " + "(" + table + ")"):
            print("Table created successfully")
            conn.commit()


def insertIntoTable():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        insert = "INSERT INTO Employee_3 (Emp_no, Emp_name) VALUES (101, 'Bolt'), (102, 'Subash');"

        if cursor.execute(insert):
            print("Values inserted successfully")
            conn.commit()


# d.	Alter the Employee name Subash to Olando
def alterTableColumn():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()
        
        alter = "UPDATE Employee_3 SET Emp_name='Olando' WHERE Emp_no=102;"

        if cursor.execute(alter):
            print("Table column modified successfully")
            conn.commit()


# e.	Also add the following to the table
# Age	Place
# 19	Chennai
# 21	Kingston
# 25	Chennai
def addColumnToTable():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()
        
        add = "ALTER TABLE Employee_3 ADD Age INT, Place VARCHAR(255)"

        if cursor.execute(add):
            print("New Columns added successfully")

            update = "UPDATE Employee_3 SET Age=19, Place='Chennai' WHERE Emp_no=101;"
            update = update + "UPDATE Employee_3 SET Age=21, Place='Kingston' WHERE Emp_no=102;"
            update = update + "INSERT INTO Employee_3 (Emp_no, Emp_name, Age, Place) VALUES (103, 'Harini', 25, 'Chennai');"

            if cursor.execute(update):
                print("Columns updated successfully")
                conn.commit()


# f.	Check the condition and retrieve the details from the table
# i.	The age from the table if the age is above 20
# ii.	The place is Chennai
# iii.	The age is above 20 and place is Chennai
def queryTable():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()
        
        ageAbove21 = "SELECT Emp_name, Age FROM Employee_3 WHERE Age > 20;"
        if cursor.execute(ageAbove21):
            print("\nThe age from the table if the age is above 20")
            for r in cursor.fetchall():
                print(r)

        place = "SELECT * FROM Employee_3 WHERE Place='Chennai';"
        if cursor.execute(place):
            print("\nWhere the place is Chennai")
            for r in cursor.fetchall():
                print(r)

        agePlace = "SELECT * FROM Employee_3 WHERE Age > 20 AND Place='Chennai';"
        if cursor.execute(agePlace):
            print("\nThe age is above 20 and place is Chennai") 
            for r in cursor.fetchall():
                print(r)   


# g. Display the sum of age as Output for the table employee
def queryG():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        # sumOfAllAges = "SELECT SUM(Age) 'Sum Of All Ages' FROM Employee_3;"
        sumOfAllAges = "SELECT Age FROM Employee_3;"
        if cursor.execute(sumOfAllAges):
            print("\nSum Of all Ages")
            for r in cursor.fetchall():
                print(r)


# h. Find the Max and Min age from the table
def queryH():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        maxAge = "SELECT MAX(Age) 'Maximum Of Ages' FROM Employee_3;"
        if cursor.execute(maxAge):
            print("\nMaximum of all Ages")
            for r in cursor.fetchall():
                print(r)

        minAge = "SELECT MIN(Age) 'Minimum Of Ages' FROM Employee_3;"
        if cursor.execute(minAge):
            print("\nMinimum Of all Ages")
            for r in cursor.fetchall():
                print(r)


# i. Display the name of the employee in Upper case
def queryI():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        upperCase = "SELECT UPPER(Emp_name) 'Employee Name' FROM Employee_3;"
        if cursor.execute(upperCase):
            print("\nMaximum and Minimum Of all Ages")
            for r in cursor.fetchall():
                print(r)


# j. Create another table Employee_prof
# Emp_no Emp_name Department          Designation Salary
# 101    Bolt     Engineering S/W     Engineer    100,000
# 102    Subash   Production Business Analyst     250,000
# 103    Harini   HR                  Admin       210,000
def queryJ():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS Employee_prof")

        table = "Emp_no INT, \nEmp_name VARCHAR(255), \nDepartment VARCHAR(255), \nDesignation VARCHAR(255), \nSalary MONEY"

        if cursor.execute("CREATE TABLE Employee_prof " + "(" + table + ")"):
            print("Table created successfully")
            
            insert = "INSERT INTO Employee_prof (Emp_no, Emp_name, Department, Designation, Salary) \
                VALUES (101, 'Bolt', 'Engineering S/W', 'Engineer', 100000), \
                    (102, 'Subash', 'Production Business', 'Analyst', 250000), \
                        (103, 'Harini', 'HR', 'Admin', 210000);"

            if cursor.execute(insert):
                print("Values inserted successfully")
                conn.commit()


# k. Using Nested blocks create a new column religion and add the following to
# the table employee

#  Create a variable and assign the values like a=”Islam”, b= “Hindu”, c=“Christian”
#  Inside the nested blocks create the conditional statements and check the nation and allocate the religion.
#  In next block count the number of people belongs to same religion.
#  Print the results.
def queryK():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()
        
        # add = "ALTER TABLE Employee_3 ADD Religion VARCHAR(255)"
        add = """
        IF COL_LENGTH('Employee_3', 'Religion') IS NULL
        BEGIN
            ALTER TABLE Employee_3 ADD Religion VARCHAR(255)
        END;
        """

        if cursor.execute(add):
            print("\n'Religion' Column added successfully")

            update = """
            DECLARE @a VARCHAR(25) = 'Islam'
            DECLARE @b VARCHAR(25) = 'Hindu'
            DECLARE @c VARCHAR(25) = 'Christian'
            --DECLARE @place VARCHAR(255) = SELECT Place FROM Employee_3

            UPDATE Employee_3
            SET Religion = (
                CASE
                    WHEN Place = 'Chennai'
                        THEN @b
                    WHEN Place = 'Kingston'
                        THEN @c
                    WHEN Place <> 'Chennai' AND Place <> 'Kingston'
                        THEN @a
                    END
            );
            """
            if cursor.execute(update):
                print("\nReligion Columns update based on religion")

                conn.commit()

        countOfPeopleRel = """
        SELECT
            Religion, COUNT(Religion) as 'Count'
        FROM
            Employee_3
        GROUP BY Religion
        """
        if cursor.execute(countOfPeopleRel):
            print("\nCount of persons belonging to the same Religion")
            for r in cursor.fetchall():
                print(r)


# l. Sort the Employee Name using the ORDER BY Clause.
def queryL():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        orderBy = """
        SELECT * FROM Employee_3 ORDER BY Emp_name
        """
        if cursor.execute(orderBy):
            print("\nUsing the ORDER BY Clause (Ascending)")
            for r in cursor.fetchall():
                print(r)
        
        orderBy = """
        SELECT * FROM Employee_3 ORDER BY Emp_name DESC
        """
        if cursor.execute(orderBy):
            print("\nUsing the ORDER BY Clause (Descending)")
            for r in cursor.fetchall():
                print(r)


# m. Also add the following to the table employee
# Department
# Engineering
# Production
# HR
def queryM():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()
        
        add = "ALTER TABLE Employee_3 ADD Department VARCHAR(255)"

        if cursor.execute(add):
            print("'Department' Column added successfully")

            update = "UPDATE Employee_3 SET Department='Engineering' WHERE Emp_no=101;"
            update += "UPDATE Employee_3 SET Department='Production' WHERE Emp_no=102;"
            update += "UPDATE Employee_3 SET Department='HR' WHERE Emp_no=103;"

            if cursor.execute(update):
                print("Columns updated successfully")
                conn.commit()


# n. Use INNER Join to create a query to display the emp_id and emp_name if the department is engineering from the table Employee and Employee_prof.
def queryN():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()
    
    query = """
    SELECT e3.Emp_no, e3.Emp_name
    FROM Employee_3 e3
        INNER JOIN Employee_prof ep
        ON ep.Emp_no = e3.Emp_no AND ep.Emp_name = e3.Emp_name
    WHERE e3.Department = 'Engineering'
    """
    if cursor.execute(query):
        print("\nUsing INNER JOIN")
        for r in cursor.fetchall():
            print(r)


# o. Use left Join to create a query to display the emp_id and Emp_name if the department is Production from the table Employee and Employee_prof
def queryO():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()
    
    query = """
    SELECT e3.Emp_no, e3.Emp_name
    FROM Employee_3 e3
        LEFT JOIN Employee_prof ep
        ON ep.Emp_no = e3.Emp_no AND ep.Emp_name = e3.Emp_name
    WHERE e3.Department = 'Production'
    """
    if cursor.execute(query):
        print("\nUsing LEFT JOIN")
        for r in cursor.fetchall():
            print(r)


# p. Find and Delete the duplicate entry in the table Employee_prof
def queryP():
    if checkConnection():
        conn = checkConnection()
        cursor = conn.cursor()

        query = "INSERT INTO Employee_prof \
            (Emp_no, Emp_name, Department, Designation, Salary)\
                VALUES (101, 'Bolt', 'Engineering S/W', 'Engineer', 100000);"
        if cursor.execute(query):
            print("\nDuplicate row is added")
            conn.commit()

            # Show duplicate entry
            query2 = "SELECT * FROM Employee_prof"
            if cursor.execute(query2):
                print("\nAll Values")
                for r in cursor.fetchall():
                    print(r)


        query3 = """
        SELECT * 
        FROM 
            (SELECT *, 
                ROW_NUMBER() OVER(PARTITION BY Emp_name ORDER BY Emp_no) Duplicates
            FROM Employee_prof
            ) AS D 
        WHERE Duplicates > 1
        """
        if cursor.execute(query3):
            print("\nAll Duplicates")
            for r in cursor.fetchall():
                print(r)

        # Delete Duplicate row
        # query4 = """
        # DELETE D 
        # FROM 
        #     (SELECT *, 
        #         ROW_NUMBER() OVER(PARTITION BY Emp_name ORDER BY Emp_no) rn 
        #     FROM Employee_prof
        #     ) AS D 
        # WHERE rn > 1
        # """
        # if cursor.execute(query4):
        #     print("\nAll Duplicates Deleted!!!")
        #     conn.commit()



def main():
    # checkConnection()
    # createTable()
    # insertIntoTable()
    # alterTableColumn()
    # addColumnToTable()
    # queryTable()

    # New Questions
    # queryG()
    # queryH()
    # queryI()
    # queryJ()
    # queryK()
    queryL()
    # queryM()
    # queryN()
    # queryO()
    # queryP()


if __name__ == "__main__":
    main()
