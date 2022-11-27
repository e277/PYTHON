# Binary file: basic operations on a binary file: open using file
# open modes (rb, rb+, wb, wb+, ab, ab+), 
# close a binary file, 
# dump() and load()
# method, 
# read, write/create, search, append and update operations in a binary
# file CSV file: 
# import csv module, open / close csv file, 
# write into a csv file
# using csv.writerow() and 
# read from a csv file using csv.reader( )

import csv


def read_binary(file_name):
    fil = open(file_name, 'rb')
    return fil.readlines()

def write_binary(file_name, binary):
    f = open(file_name, 'wb')
    f.write(binary)
    f.close()
    # lines = read_binary('bin_file.txt')
    # print(lines)
    # f_bin = open('bin_file.bin', 'wb')
    
    # print("Binary written successfully")
    # print("Binary data:", f_bin.readlines())

def to_csv():
    fil = open('bin_file.bin', 'w')
    writer = csv.writer(fil)
    # writer.writero   ws([["a", 1], ["b", 2], ["c", 3], ["d",4]])
    writer.writerows()
    fil.close()
    
    read_binary()
    

if __name__ == "__main__":
    print(read_binary('bin_file.txt'))
    write_binary('bin_file.txt', 'bin_file.bin')
    # print(to_csv())
    