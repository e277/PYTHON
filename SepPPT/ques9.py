# 3. Write a program to read a four-digit number through the keyboard and calculate the sum of its digits
def cal_sum_of_digits():
    read_input = int(input("Enter a four-digit number: "))
    sum = 0
    for digit in str(read_input):
        sum += int(digit)
    return sum

if __name__ == '__main__':
    print("The sum of the digits: ", cal_sum_of_digits())