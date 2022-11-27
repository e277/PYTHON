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

if __name__ == '__main__':
    cal_time(1.5)