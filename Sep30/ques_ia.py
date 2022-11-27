# A while loop that asks the user for a number, and prints a countdown from that number to zero.
def count_down(number):
    if number == 0:
        return
    else:
        print(number)
        count_down(number - 1)

if __name__ == "__main__":
    input_num = int(input("Enter a number: "))
    print("\nCounting down from:", input_num)
    count_down(input_num)
    print("Finished counting down from:", input_num)