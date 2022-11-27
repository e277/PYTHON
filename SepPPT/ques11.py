# 5. Write a program to calculate age based on input of date, month and year.
from datetime import date

def cal_age(dob):
    today_dt = date.today()
    your_age = today_dt.year - dob.year - ((today_dt.month, today_dt.day) < (dob.month, dob.day))
    print("You are {} years old".format(your_age))

if __name__ == '__main__':
    cal_age(date(1997, 1, 28))