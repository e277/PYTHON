import pickle
import csv


def append_employee():

    with open('employees.csv', 'ab+', newline='') as csvfile:
        print("Add Employee")
    
        fieldnames = ['Employee Id', 'Employee Name', 'Salary', 'Job Title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        emp_id = int(input("Enter the Employee Id: "))
        emp_name = input("Enter Employee Name: ")
        salary = float(input("Enter Employee Salary: "))
        job_title = input("Enter Employee Job Title: ")

        writer.writeheader()
        writer.writerow({
            'Employee Id': emp_id,
            'Employee Name': emp_name,
            'Salary': salary,
            'Job Title': job_title
        })



def read_employee():
    f = open('employees.csv', 'rb+')
    print("*" * 50)
    print("Data stored in File....")
    while True:
        try:
            emp_record = pickle.load(f)
            print("Employee Id: ", emp_record['emp_id'])
            print("Employee Name: ", emp_record['emp_name'])
            print("Employee Salary: ", emp_record['salary'])
            print("Employee Job Title: ", emp_record['job_title'])
            print("." * 50)
        except Exception:
            break

        f.close()


def search_employee():
    f = open("employees.csv", "rb")
    pc = int(input("Enter Employee Id to Search: "))
    flag = False

    while True:
        try:
            emp_record = pickle.load(f)
            if emp_record['emp_id'] == pc:
                print("Employee Name: ", emp_record['emp_name'])
                print("Employee Salary: ", emp_record['salary'])
                print("Employee Job Title: ", emp_record['job_title'])
                flag = True
        except Exception:
            break
    if flag == False:
        print("Record not found...")

    f.close()


def update_employee():
    f = open('employees.csv', 'rb')
    emp_record_list = []
    while True:
        try:
            emp_record = pickle.load(f)
            emp_record_list.append(emp_record)
        except EOFError:
            break

    f.close()

    e_id = int(input("Enter Employee Id to Update: "))
    e_nm = input("Enter new Employee Name: ")
    e_sal = double(input("Enter Salary: "))
    e_jt = input("Enter Job Title: ")

    for i in range(len(emp_record_list)):
        if emp_record_list[i]['emp_id'] == e_id:
            emp_record_list[i]['emp_name'] = e_nm
            emp_record_list[i]['salary'] = e_sal
            emp_record_list[i]['job_title'] = e_jt

    f = open('employees.csv', 'wb')

    for i in emp_record_list:
        pickle.dump(i, f)

    f.close()


def delete_employee():
    f = open('employees.csv', 'rb')
    emp_record_list = []
    while True:
        try:
            emp_record = pickle.load(f)
            emp_record_list.append(emp_record)
        except EOFError:
            break

    f.close()

    e_id = int(input("Enter Employee Id to delete record: "))

    f = open('employees.csv', 'wb')

    for i in emp_record_list:
        if i['emp_id'] == e_id:
            continue
        pickle.dump(i, f)

    f.close()


def main():
    while True:
        print('1. Insert Record')
        print('2. Display Records')
        print('3. Search Record')
        print('4. Update Record')
        print('5. Delete Record')
        print('0. Exit')
        
        choice = int(input('Enter you choice: '))
        if choice == 0:
            break
        elif choice == 1:
            append_employee()
        elif choice == 2:
            read_employee()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            delete_employee()


if __name__ == "__main__":
    main()