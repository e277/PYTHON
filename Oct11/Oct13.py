# opening a text file, text file open modes (r, r+, w, w+, a, a+), 
# closing a text file, 
# opening a file using with clause, 
# writing/appending data to a text file using write() and writelines()

import sys


def writeToFile():
    f = open("out 13.txt", "w")
    f.write("This is the write command")
    f.write("It allows us to write in a particular file")
    f.close()

def writeToFile2():
    f = open("out 13.txt", "w")
    f.writelines(["This is line 1"], ["This is line 2"])
    f.close()

def readFromFile():
    pass

def readFromFile2():
    pass

def appendToFile():
    pass

def appendToFile2():
    pass

def fileWith():
    pass

def fileWith2():
    pass


def main():
    print("""
    1 - write (w)
    2 - write and read (w+)
    3 - read (r)
    4 - read and write (r+)
    5 - append (a)
    6 - append and read (a+)
    7 - write using 'with'
    8 - read using 'with'
    0 - Exit
    """)

    option = int(input("Choose option: "))

    match option:
        case 0:
            print("Invalid Option")
            sys.exit()
        case 1:
            readFromFile()
        case 2:
            readFromFile2()
        case 3:
            writeToFile()
        case 4:
            writeToFile2()
        case 5:
            appendToFile()
        case 6:
            appendToFile2()



if __name__ == "__main__":
    main()
