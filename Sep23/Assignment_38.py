# write a Python code to find the Maximum of these two numbers.
# Examples:
# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1

# Method #1: This is the naive approach where we will compare two numbers using if-else statement and will print the output accordingly
def find_max_1(a, b):
    if a == b:
        return "Both are equal"
    elif a > b:
        return "a greater than b"
    elif a < b:
        return "a less than b"

if __name__ == '__main__':
    print("\nMethod 1")
    print(find_max_1(2, 4))
    print(find_max_1(-1, -4))


# Method #2: Using max() function
# This function is used to find the maximum of the values passed as its arguments.
def find_max_2(a, b):
    return max(a, b)

if __name__ == '__main__':
    print("\nMethod 2")
    print("The maximum of two numbers is:", find_max_2(2, 4))
    print("The maximum of two numbers is:", find_max_2(-1, -4))


# Method #3: Using Ternary Operator
# This operator is also known as conditional expression are operators that evaluate something based on a condition being true or false. It simply allows testing a condition in a single line
def find_max_3(a, b):
    return "a is greater than b" if a > b else "a is less than b"

if __name__ == '__main__':
    print("\nMethod 3")
    print(find_max_3(2, 4))
    print(find_max_3(-1, -4))


# Method #4: Using lambda function
find_max_4 = lambda a, b: max(a, b)

if __name__ == '__main__':
    print("\nMethod 4")
    # print("The maximum of two numbers is:", find_max_4())
    # print("The maximum of two numbers is:", find_max_4())
    print("The maximum of two numbers is:", find_max_4(2, 4))
    print("The maximum of two numbers is:", find_max_4(-1, -4))


# Method #5: Using list comprehension
def find_max_5(a, b):
    result = [a if a > b else b]
    return result

if __name__ == '__main__':
    print("\nMethod 5")
    print("The maximum of two numbers is:", find_max_5(2, 4))
    print("The maximum of two numbers is:", find_max_5(-1, -4))