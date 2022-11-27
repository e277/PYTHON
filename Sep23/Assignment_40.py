# Python Program for Maximum height when coins are arranged in a triangle
# Input : N = 7
# Output : 3
# Maximum height will be 3, putting 1, 2 and then 3 coins. It is not possible to use 1 coin left.
# Input : N = 12
# Output : 4
# Maximum height will be 4, putting 1, 2, 3 and coins, it is not possible to make height as 5,
# because that will require 15 coins

def sq_root(val):
    num = val
    m = 1
    e = 0.000001
    while num - m > e:
        num = (num + m) / 2
        m = val / num
    return num

def find_max_height(number):
    val = 1 + 8 * number
    max_height = int((-1 + sq_root(val)) / 2)
    return max_height

if __name__ == "__main__":
    print("The maximum height of triangle is:", find_max_height(7))
    print("The maximum height of triangle is:", find_max_height(12))
