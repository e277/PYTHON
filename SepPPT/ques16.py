# 5. Using python code :
#    Write a code for the following output
#    Input: 1
#    Given 2 ints, A=10 and B=20
#    Output: 1 True

#    Input: 2
#    Given 2 ints, A=20 and B=20
#    Output: 2 False

#    Input: 3
#    Given 2 ints, A=7 and B=3
#    Output: 3 True

# (Note: return True if one if them is 10 or if their sum is 10.)
def check_num(num1, num2):
    if num1 == num2:
        return False
    elif num1 == 10 or num2 == 10:
        return True
    elif (num1 + num2) == 10:
        return True

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(check_num(num1, num2))
    # print(check_num(10, 20))
    # print(check_num(20, 20))
    # print(check_num(7, 3))