# 4. An ATM contains Indian currency notes of 100, 500 and 1000. To withdraw cash from this
#    ATM, the user has to enter the number of notes he/she wants of each currency, i.e. of 100,
#    500 and 1000. Write a program to calculate the total amount withdrawn by the person
#    from the ATM in rupees.
def cal_atm(amount):
    notes = [1000, 500, 100]
    count = {}

    for note in notes:
        if amount >= note:
            count[note] = amount // note
            amount = amount % note
        
    print("Notes")
    for key, value in count.items():
        print(f"{key} = {value}")

if __name__ == "__main__":
    cal_atm(1700)