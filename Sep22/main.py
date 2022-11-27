import module

def main():
    option = int(input("Choose 1-Addition, 2-Multiplication or 3-Subtraction of Matrix: "))

    if option == 1:
        module.add_matrix()
    elif option == 2:
        module.mul_matrix()
    elif option == 3:
        module.sub_matrix()
    else:
        raise ValueError("Unknown option %d" % option)

    return

if __name__ == '__main__':
    main()