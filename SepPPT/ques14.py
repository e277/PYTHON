# 3. Write python code for the following
#    Input:
#    An int n,
#    Output:
#    return True if it the given number is near to 100.
def near_100(num):
    if num <= 105 and num >= 95:
        return True
    return False

if __name__ == "__main__":
    print(near_100(90))