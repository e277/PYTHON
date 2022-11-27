# 1. Write a Python Program for displaying the following pattern
#    5
#    5 4 3
#    5 4 3 2
#    5 4 3 2 1
def dis_pattern(num_of_rows):
    for i in range(num_of_rows, 0, -1):
        for j in range(num_of_rows, i-1, -1):
            print(j, end='')
        print()

if __name__ == '__main__':
    dis_pattern(5)