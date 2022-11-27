# 4. From the given int n, return the absolute difference between n and 10, 
# except return double the absolute difference if n is over 10.
def absolute_difference(n, check=10):
    if n < check:
        return abs(n - check)
    return 2 * abs(n - check)

if __name__ == '__main__':
    print(absolute_difference(9))
    print(absolute_difference(19))