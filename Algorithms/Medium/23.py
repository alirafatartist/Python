def matrix_transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)
    return transposed

print(matrix_transpose([
    [1, 2],
    [3, 4],
    [5, 6]
    ]))  # Output: [[1, 3, 5], [2, 4, 6]]

print(matrix_transpose([
    [1, 3, 5],
    [2, 4, 6]
    ]))
# Output: [
    # [1, 2],
    # [3, 4],
    # [5, 6]
    # ]