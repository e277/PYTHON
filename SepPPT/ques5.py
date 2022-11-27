# 5. Program to print the MSB digit of given number {Input:1567 Output:1}
def msb_digit(num):
    if (num == 0): return 0;
 
    msb = 0;
    num = int(num / 2);
 
    while (num > 0):
        num = int(num / 2);
        msb += 1;
 
    return (1 << msb);

if __name__ == '__main__':
    # cal_nums()
    # add_decimal_parts(2.356, 3.5678)
    # cal_time(1.5)
    # unit_digit(1567)
    print(msb_digit(1567))
    # cal_sum_bet_nums(5, 10)