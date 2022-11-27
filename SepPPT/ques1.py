# 1. Collect three run-time input from user. Add together the first two numbers and then multiply
#    this total by the third. Display the answer as “The answer is :“ [answer]

def cal_nums():
    numbers = []
    for i in range(0, 3):
        input_number = int(input("Enter number: "))
        numbers.append(input_number)
    # print("Numbers:", numbers)
    answer = (numbers[0] + numbers[1]) * numbers[2]
    print("The answer of: ({} + {}) * {}".format(numbers[0], numbers[1], numbers[2]), "is equal to", answer)


if __name__ == '__main__':
    cal_nums()
   