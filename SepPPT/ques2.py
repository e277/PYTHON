# 2. Program to print only the added fraction of any two number {Input: 2.356 3.5678 Output: 0.9238}
def add_decimal_parts(num1, num2):
    for i in range(0, 2):
        int_1, dec_1 = int(num1), num1 - int(num1)
        int_2, dec_2 = int(num2), num2 - int(num2)
        
    result = dec_1 + dec_2
    print("The result of the decimal part is:", result)

if __name__ == '__main__':
    add_decimal_parts(2.356, 3.5678)
