
def add_matrix():
    row_1 = int(input("Enter number of rows for first matrix: "))
    col_1 = int(input("Enter number of columns for first matrix: "))
    print("Enter the elements of First Matrix:")
    matrix_1= [[int(input()) for i in range(col_1)] for i in range(row_1)]
    print("First Matrix is: ")
    for n in matrix_1:
        print(n)

    row_2 = int(input("Enter number of rows for second matrix: "))
    col_2 = int(input("Enter number of columns for second matrix: "))
    print("Enter the elements of Second Matrix:")
    matrix_2 = [[int(input()) for i in range(col_2)] for i in range(row_2)]
    for n in matrix_2:
        print(n)
        
    result = [[0 for i in range(col_1)] for i in range(row_1)]
    result = [[0 for i in range(col_2)] for i in range(row_2)]

    if row_1 != col_2:
        raise ValueError("Row and columns must be the same")
    
    for i in range(col_1):
        for j in range(row_2):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]

    print("The Addition of Above two Matrices is : ")
    for r in result:
        print(r)



def sub_matrix():
    row_1 = int(input("Enter number of rows for first matrix: "))
    col_1 = int(input("Enter number of columns for first matrix: "))
    print("Enter the elements of First Matrix:")
    matrix_1= [[int(input()) for i in range(col_1)] for i in range(row_1)]
    print("First Matrix is: ")
    for n in matrix_1:
        print(n)

    row_2 = int(input("Enter number of rows for second matrix: "))
    col_2 = int(input("Enter number of columns for second matrix: "))
    print("Enter the elements of Second Matrix:")
    matrix_2 = [[int(input()) for i in range(col_2)] for i in range(row_2)]
    for n in matrix_2:
        print(n)
        
    result = [[0 for i in range(col_1)] for i in range(row_1)]
    result = [[0 for i in range(col_2)] for i in range(row_2)]

    if row_1 != col_2:
        raise ValueError("Row and columns must be the same")
    
    for i in range(col_1):
        for j in range(row_2):
            result[i][j] = matrix_1[i][j] - matrix_2[i][j]

    print("The Subtraction of Above two Matrices is : ")
    for r in result:
        print(r)



def mul_matrix():
    row_1 = int(input("Enter number of rows for first matrix: "))
    col_1 = int(input("Enter number of columns for first matrix: "))
    print("Enter the elements of First Matrix:")
    matrix_1= [[int(input()) for i in range(col_1)] for i in range(row_1)]
    print("First Matrix is: ")
    for n in matrix_1:
        print(n)

    row_2 = int(input("Enter number of rows for second matrix: "))
    col_2 = int(input("Enter number of columns for second matrix: "))
    print("Enter the elements of Second Matrix:")
    matrix_2 = [[int(input()) for i in range(col_2)] for i in range(row_2)]
    for n in matrix_2:
        print(n)
        
    result = [[0 for i in range(col_1)] for i in range(row_1)]
    result = [[0 for i in range(col_2)] for i in range(row_2)]

    if row_1 != col_2:
        raise ValueError("Row and columns must be the same")

    for i in range(len(matrix_1)):
        for j in range(col_2):
            for k in range(row_2):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]

    print("The Multiplication of Above two Matrices is : ")
    for r in result:
        print(r)

