import collections
import pprint


# 5. a) Write a program to count frequency of characters in a given file. (5 marks)
def partA():
    file_input = 'quest5.txt'
    with open(file_input, 'r') as info:
        count = collections.Counter(info.read().upper())
        value = pprint.pformat(count)
    print("\n" + value)


# b) Use the character frequency to tell whether the given file is a Python program file,
# C program file or a text file?
def partB():
    try:
        file_input = 'quest5.txt'
        name_ext = file_input.split(".")

        if name_ext[1] == ".py":
            print("Python file")
        elif name_ext[1] == "c":
            print("C file")
        elif name_ext[1] == "txt":
            print("\nText file")
    except Exception as e:
        print(e)

def main():
    partA()
    partB()

if __name__ == "__main__":
    main()