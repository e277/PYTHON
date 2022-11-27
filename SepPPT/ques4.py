# 4. Program to print the unit digit of a given number { Input: 1567 Output: 7}
def unit_digit(num):
    num = str(num)
    print(num[-1])

if __name__ == '__main__':
    unit_digit(1567)