# 4. Write a function that accepts a collection of students and verifes/validates the information
# for each student in the collection according to the following criteria:
# a. Each student must have a full name (first name and last name separated by space, verify that there are 2 words)
# b. Each student must have an Id (6 numeric characters)
# c. Each student must have an Age (must be in inclusive range 18 to 35)
# d. Each student must have an Average (must be in inclusive range 0 to 100)
import csv


def question4():
    pass


# 5. Read and display the contents of the Data.csv
def read_contents(file_name):
    with open(file_name) as f:
        return f.read()


# 6. Print the name and the number entries for each country from Data.csv
def display_name_entries(file_name):
    with open(file_name) as f:
        file = csv.DictReader(f)
        country = []
        freq = {}
        
        for col in file:
            country.append(col['Country'])
        print(country)

        for ctry in country:
            freq[ctry] = country.count(ctry)
            
        for k in freq.items():
            print(k)


# 7. Print the average salary from the salary column in Data.csv
def avg_salary(file_name):
    sal_list = []
    with open(file_name) as f:
        read = csv.DictReader(f)
        
        for col in read:
            sal = col["Salary"]
            if sal is not None and sal is not "":
                sal_list.append(int(col["Salary"]))

    a_sal = sum(sal_list) / len(sal_list)
    
    return a_sal # 63,777.778


# 8. Wrtite 3 new entries to the Data.csv (set the country to Jamaica for each entries)
def add_3_entries(file_name, list_of_entries):
    with open(file_name, 'a', newline='\n') as f:
        write = csv.writer(f)
        write.writerow(list_of_entries)


# CALLING THE FUNCTIONS
if __name__ == "__main__":
    # question4()
    # print(read_contents("Data.csv"))
    display_name_entries("Data.csv")
    # print(avg_salary("Data.csv"))
    # add_3_entries("Data.csv", ['Jamaica', 25, 49000, 'Yes'])
    # add_3_entries("Data.csv", ['Jamaica', 52, 89000, 'No'])
    # add_3_entries("Data.csv", ['Jamaica', 25, 99000, 'Yes'])

