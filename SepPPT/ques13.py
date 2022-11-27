# 2. A
#    A B
#    A B C
#    A B C D
#    A B C D E
def dis_pattern_let():
    for i in range(1, 6):
        for j in range(65, 65+i):
            a = chr(j)
            print(a, end='')
        print()

if __name__ == '__main__':
    dis_pattern_let()