# 6. Program to calculate the sum from ‘M’ number to ‘N’ number. {Input: M-5 N-10 Output: 45}
def cal_sum_bet_nums(num1, num2, sum=0):
    for i in range(num1, num2 + 1):
        sum += i
    print("The sum of numbers between(inclusively):", num1, "and", num2, "is", sum)

if __name__ == '__main__':
    cal_sum_bet_nums(5, 10)