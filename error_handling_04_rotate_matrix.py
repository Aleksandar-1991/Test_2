class MatrixContentError(Exception):
    pass
class MatrixSizeError(Exception):
    pass

def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        if len(matrix[i]) != len(matrix):
            raise MatrixSizeError("The size of the matrix is not a perfect square")
        for j in range(i, matrix_length):
            if not matrix[i][j].isdigit():
                raise MatrixContentError("The matrix must consist of only integers")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()

    if not line:
        break
    mtrx.append(line)

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
