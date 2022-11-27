import copy
import decimal
import random
import types

# 1. Write a Python program to shuffle the elements of a given list. Use random.shuffle()
def shuffle(list1):
    random.shuffle(list1)
    return list1

print()
print("<< QUESTION 1 >>")
list1 = [1,4,6,9]
print("Original:", list1)
print("Shuffle:", shuffle(list1))
print()


# 2. Write a Python program to check if a given function is a generator or not. 
# Use types.GeneratorType()
def greet_1(greet):
    print(greet)
    print("After greeting")
    print(greet)

def greet_2(greet):
    print(greet)
    yield 1
    print(greet)
    yield 2

print("<< QUESTION 2 >>")
# print("Is Generator: ", isinstance(greet_1('Hello ungu'), types.GeneratorType))
# print("Is Generator: ", isinstance(greet_2('Hello ezra'), types.GeneratorType))

# greet_1("Hello Ezra!!!")
print(next(greet_2("Hello Ezra!!!")))
print(next(greet_2("Hello Ezr!!!")))

print()


# 3. Write a Python program to configure the rounding to round to the nearest 
# - with ties going towards 0, with ties going away from 0. 
# Use decimal.ROUND_HALF_DOWN, decimal.ROUND_HALF_UP
def round_up(val_1):
    con_1 = decimal.Decimal(val_1)
    out_1 = decimal.Decimal(con_1.quantize(decimal.Decimal('0'), rounding=decimal.ROUND_HALF_UP))
    return out_1

print("<< QUESTION 3 >>")
print("ROUND_HALF_UP: ", round_up(3.55))


def round_down(val_2):
    con_2 = decimal.Decimal(val_2)
    out_2 = decimal.Decimal(con_2.quantize(decimal.Decimal('0'), rounding=decimal.ROUND_HALF_DOWN))
    return out_2


print("ROUND_HALF_DOWN: ", round_down(3.24))
print()


# 4. Write a Python program to create a shallow and deep copy of a
# given dictionary. Use copy.copy
def shallow_deep_copy(dictionary_1):
    print("ID:", id(dictionary_1), "Original:", dictionary_1)

    s_copy = copy.copy(dictionary_1)
    d_copy = copy.deepcopy(dictionary_1)
    print("ID:", id(s_copy), "Shallow copy:", s_copy)
    print("ID:", id(d_copy), "Deep copy:", d_copy)
    print()

    dictionary_1.update({"age": 30})

    print("ID:", id(dictionary_1), "Value:", dictionary_1)
    print("ID:", id(s_copy), "Value:", s_copy)
    print("ID:", id(d_copy), "Value:", d_copy)

print("<< QUESTION 4 >>")
shallow_deep_copy({"name": "Ezra", "age": 20})
print()


# 5. Write a Python program to count the number of lines in 
# a given CSV file. Use csv.reader
def count_lines(csv_file):
    # DataCleansingAct\no_moh_data.csv
    count = 1
    with open(csv_file, 'r') as csv_reader:
        for line in csv_reader.read().splitlines():
            count += 1
    return count

print("<< QUESTION 5 >>")
print("The number of lines in file:", count_lines('DataCleansingAct\\no_moh_data.csv'))
print()
