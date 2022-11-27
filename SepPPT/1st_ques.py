# 1. Collect three run-time input from user. Add together the first two numbers and then multiply
#    this total by the third. Display the answer as “The answer is :“ [answer]
from ast import Num


def cal_nums():
    numbers = []
    for i in range(0, 3):
        input_number = int(input("Enter number: "))
        numbers.append(input_number)
    # print("Numbers:", numbers)
    answer = (numbers[0] + numbers[1]) * numbers[2]
    print("The answer is:", answer)

# 2. Program to print only the added fraction of any two number {Input: 2.356 3.5678 Output:
#    0.9238}
def add_decimal_parts(num1, num2):
    for i in range(0, 2):
        int_1, dec_1 = int(num1), num1 - int(num1)
        int_2, dec_2 = int(num2), num2 - int(num2)
        
    result = dec_1 + dec_2
    print("The result of the decimal part is:", result)


# 3. Program to calculate hours, minutes and seconds for a given input days.
def cal_time(no_of_days, apply_zeroes=1):
    print("Calculating days to hh:mm:ss for,", no_of_days, "days")
    secs = no_of_days * 24 * 60 * 60

    def zeroes(num):
        if num < 10:
            num = "0"+num
        return num

    sec = secs % 60
    min_ = secs // 60 % 60
    hrs = secs // 3600
    if apply_zeroes > 0:
        sec = zeroes(hrs)
    
    print("{}:{}:{}".format(hrs, min_, sec))


# 4. Program to print the unit digit of a given number { Input: 1567 Output: 7}
def unit_digit(num):
    num = str(num)
    print(num[-1])


# 5. Program to print the MSB digit of given number {Input:1567 Output:1}
def msb_digit(num):
    if (num == 0): return 0;
 
    msb = 0;
    num = int(num / 2);
 
    while (num > 0):
        num = int(num / 2);
        msb += 1;
 
    return (1 << msb);

# 6. Program to calculate the sum from ‘M’ number to ‘N’ number. {Input: M-5 N-10 Output: 45}
def cal_sum_bet_nums(num1, num2, sum=0):
    for i in range(num1, num2 + 1):
        sum += i
    print(sum)

if __name__ == '__main__':
    # cal_nums()
    # add_decimal_parts(2.356, 3.5678)
    # cal_time(1.5)
    # unit_digit(1567)
    print(msb_digit(1567))
    # cal_sum_bet_nums(5, 10)