import csv
import json
import sys
import xml.etree.ElementTree as ET


# 1. To read 2and 3 columns of a given CSV file and print the content of the column
def quest1():
    print('Read Two columns of a CSV file')
    with open('Data.csv', newline='') as cf:
        data = csv.DictReader(cf, delimiter=',')
        print('Age Salary')
        for r in data:
            print(r['Age'], r['Salary'])
        
    print('\nRead Three Columns of a CSV file')
    with open('Data.csv', newline='') as cf2:
        data2 = csv.DictReader(cf2, delimiter=',')
        print('Country Age Salary')
        for r2 in data2:
            print(r['Country'], r2['Age'], r2['Salary'])


# 2. To write a Python dictionary to a csv file. After writing the CSV file read the CSV file and
# display the content
def quest2():
    csv_columns = ['Student_ID','Mark_One', 'Mark_Two', 'Mark_Three', 'Mark_Four', 'Mark_Five']
    dict_data = {'Student_ID':['1', '2', '3'],
        'Mark_One':[33, 25, 56],
        'Mark_Two':[35, 30, 30],
        'Mark_Three':[21, 40, 55],
        'Mark_Four':[71, 25, 55],
        'Mark_Five':[10, 10, 40], }

    try:
        with open("temp.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(dict_data)
    except IOError:
        print("I/O error")

    data = csv.DictReader(open("./temp.csv"))
    print("CSV file as a dictionary:\n")
    for row in data:
        print(row)


# 3. To read a given CSV file as a list.
def quest3():
    filename = input("Enter file name: ")
    with open(filename, newline='') as cf3:
        reader = csv.reader(cf3)
        csv_list = list(reader)
    
    print("CSV file as a list:\n", csv_list)


# 4. Display the elements in XML using python with for loop.
def quest4():
    tree = ET.parse('Data.xml')
    root = tree.getroot()

    for book in root:
        print(book.attrib)


# 5. With the findall() method work the Parse XML files in Python
def quest5():
    tree = ET.parse('Data.xml')
    root = tree.getroot()
    
    for book in root.findall('book'):
        title = book.find("title").text
        price = book.find("price").text
        print(title, price)


# 6. Write python code to operate on JSON files for the following:
def quest6():
    old_data = {
        "person" : [
            {
                "firstName": "John",
                "lastName": "Constantine",
                "hobbies": ["magic", "dark arts", "con-artist"],
                "age": 35,
                "children": [
                    {
                        "firstName": "Alice",
                        "age": 6
                    },
                    {
                        "firstName": "Bob",
                        "age": 8
                    }
                ]
            }
        ]
    }

    print("\
    Options\
    1 - loads()\
    2 - load()\
    3 - dumps()\
    4 - dump()\
    5 - Write to Json file\
    0 - Exit\
    ")

    option = input("Enter Number: ")

    match int(option):
        case 0:
            sys.exit(0)

        case 1:
            # a. json.loads()
            json_string_loads = json.dumps(data, indent=4)
            print(json_string_loads)            
        
        case 2:
            # b. json.load()
            f = open("Data.json", "r")
            data = json.load(f, indent=4)
            for i in data['person']:
                print(i)
            f.close()

        case 3:
            # c. json.dumps()
            json_string = json.dumps(data, indent=4)
            print(json_string)

        case 4:
            # dump
            f = open("Data.json", "w")
            json.dump(old_data, f, indent=4)
            f.close()

        case 5:
            # d. Write JSON to a file
            new_data = {
                "firstName": "Ezra",
                "lastName": "Muir",
                "hobbies": ["reading", "introspecting", "music"],
                "age": 25,
                "children": None
            }

            with open("Data.json", "r+") as append_file:
                data = json.load(append_file)
                data["person"].append(new_data)
                append_file.seek(0)
                json.dump(data, append_file, indent=4)



def main():
    # quest1()
    # quest2()
    # quest3()
    quest4()
    quest5()
    # quest6()


if __name__ == "__main__":
    main()

