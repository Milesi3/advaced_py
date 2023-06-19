# Транспонирование матрицы

def transpose_matrix(matrix):
    matrix_rotate = tuple(zip(*matrix[::-1]))
    return matrix_rotate

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(element) for element in row))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = transpose_matrix(matrix)
print_matrix(transposed)
