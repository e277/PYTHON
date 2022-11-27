# 1. Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# If n is greater than 100 raise a value error indicating that the number is too large
def check_number(n):
    if n < 1:
        return -1
        # raise ValueError("Negative number not accepted...")
    elif n%2 == 1:
        return "Weird"
    elif n%2 == 0 and (n >= 2 and n <= 5):
        return "Not Weird"
    elif n%2 == 0 and (n >= 6 and n <= 20):
        return "Weird"
    elif n%2 == 0 and (n > 20 and n <= 100):
        return "Not Weird"
    else:
        raise ValueError("The number is too large..")


# if __name__ == "__main__":
#     input_number = int(input("Number: "))
#     print(check_number(input_number))


# 3. When rolling a dice the result may be any random number in the inclusive range of 1 to 6. 
# Sara is running an experiment to see how many times each number will occur if she rolls 
# the dice 100 times. Write a program to simulate Sara's experiment.
# Print the result of the experiment.
import random


def roll_dice():
    frequency = {}
    dices = [1,2,3,4,5,6]
    choices = []

    for i in range(1, 101):
        # print(i)
        rolls = random.choice(dices)
        # print(rolls)
        choices.append(rolls)
    # print(choices)

    for j in choices:
        frequency[j] = choices.count(j)

    for key, value in frequency.items():
        print(f'{key} repeated {value} times')


if __name__ == "__main__":
    roll_dice()


# 2. Write a function that prompts a user to enter a value n.
# if n is an odd integer return n2
# if n is an even integer return n3
# if n is not an integer raise a type error and prompt the user to enter another value
def num_man(n):
    if n < 1:
        return -1
    elif n%2 == 1:
        return n**2
    elif n%2 == 0:
        return n**3
    # elif isinstance(n, int):
    #     raise ValueError("Not an integer...")


# if __name__ == "__main__":
#     while True:
#         try:
#             input_number = int(input("Number: "))
#             print(num_man(input_number))
#             break
#         except ValueError:
#             print("Not an integer")
