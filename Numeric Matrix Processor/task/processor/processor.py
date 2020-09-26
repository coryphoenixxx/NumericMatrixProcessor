def print_matrix(m):
    for i in range(len(m)):
        print(' '.join(map(str, m[i])))
    print()


def enter_matrix(intro, n_rows):
    print(intro)
    matrix = []
    for _ in range(n_rows):
        row_input = input()
        if '.' in row_input:
            matrix.append(list(map(float, row_input.split())))
        else:
            matrix.append(list(map(int, row_input.split())))
    return matrix


def dot_product(m1, row, m2, col):
    s = 0
    m1_row = m1[row]
    m2_col = [m2[i][col] for i in range(len(m2))]
    for i in range(len(m1_row)):
        s += m1_row[i] * m2_col[i]
    return s


def add_matrices():
    n1, m1 = list(map(int, input("Enter size of first matrix: ").split()))
    matrix1 = enter_matrix("Enter first matrix:", n1)
    n2, m2 = list(map(int, input("Enter size of second matrix: ").split()))
    matrix2 = enter_matrix("Enter second matrix:", n2)
    for i in range(n1):
        for j in range(m1):
            matrix1[i][j] += matrix2[i][j]
    print("The result is:")
    print_matrix(matrix1)


def mul_matrix_by_const():
    n, m = list(map(int, input("Enter size of matrix: ").split()))
    matrix = enter_matrix("Enter matrix:", n)

    const = input("Enter constant: ")
    if '.' in const:
        const = float(const)
    else:
        const = int(const)
    for i in range(n):
        for j in range(m):
            matrix[i][j] *= const
    print("The result is:")
    print_matrix(matrix)


def mul_matrices():
    n1, m1 = list(map(int, input("Enter size of first matrix: ").split()))
    matrix1 = enter_matrix("Enter first matrix:", n1)

    n2, m2 = list(map(int, input("Enter size of second matrix: ").split()))
    if m1 == n2:
        res_matrix = [[0 for _ in range(m2)] for _ in range(n1)]
        matrix2 = enter_matrix("Enter second matrix:", n2)
        for i in range(n1):
            for j in range(m2):
                res_matrix[i][j] = dot_product(matrix1, i, matrix2, j)
        print("The result is:")
        print_matrix(res_matrix)
    else:
        print("The operation cannot be performed.\n")


def transpose_matrix():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    res_matrix = []
    trans_choice = input("Your choice: ")
    n, m = list(map(int, input("Enter size of matrix: ").split()))
    matrix = enter_matrix("Enter matrix:", n)
    if trans_choice == '1':
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            res_matrix.append(row)
    if trans_choice == '2':
        for j in range(len(matrix[0])-1, -1, -1):
            row = []
            for i in range(len(matrix)-1, -1, -1):
                row.append(matrix[i][j])
            res_matrix.append(row)
    if trans_choice == '3':
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)-1, -1, -1):
                row.append(matrix[j][i])
            res_matrix.append(row)
    if trans_choice == '4':
        for j in range(len(matrix[0])-1, -1, -1):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[j][i])
            res_matrix.append(row)
    print_matrix(res_matrix)


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit""")
    try:
        choice = input("Your choice: ")
        if choice == '0':
            break
        if choice == '1':
            add_matrices()
        if choice == '2':
            mul_matrix_by_const()
        if choice == '3':
            mul_matrices()
        if choice == '4':
            transpose_matrix()
    except:
        print("The operation cannot be performed.\n")