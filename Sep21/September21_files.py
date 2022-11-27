# Exercise
def open_file(filename):
    with open(filename) as f:
        return f.read()

def read_3_character(filename):
    with open(filename) as f:
        return f.read(3)

def read_1_line(filename):
    with open(filename) as f:
        return f.readline()

def read_2_lines(filename):
    count_lines = 0
    with open(filename) as f:
        for line in f.readlines():
            count_lines += 1
            print(line, end='')
            if count_lines == 2:
                break

def add_to_file(filename, data=''):
    with open(filename, 'a+') as f:
        f.write("\n" + data)
        print("Check file %s" % filename)

def close_file(filename): # Because I am using with, I don't need close_file
    pass

def main():
    print("---OPTIONS---")
    print("1 - Read from file ")
    print("2 - Read first 3 characters from file ")
    print("3 - Read one line from file ")
    print("4 - Read two lines from file ")
    print("5 - Add to file ")
    print("6 - Close to file ")
    option = int(input("Enter option: "))
    
    if option == 1:
        print(open_file('Sep_Learn\september21.txt'))
    elif option == 2:
        print(read_3_character('Sep_Learn\september21.txt'))
    elif option == 3:
        print(read_1_line('Sep_Learn\september21.txt'))
    elif option == 4:
        read_2_lines('Sep_Learn\september21.txt')
    elif option == 5:
        add_to_file('Sep_Learn\september21.txt', "And now I'm adding more things!!!")
    elif option == 6:
        print(close_file())
    else:
        print("Not an option")

if __name__ == '__main__':
    main()