# Транспонирование матрицы

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с перевернутыми размерностями
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(element) for element in row))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = transpose_matrix(matrix)
print_matrix(transposed)
