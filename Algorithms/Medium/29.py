def pivot_simplex(tableau, pivot_row, pivot_col):
    pivot_value = tableau[pivot_row][pivot_col]
    
    # Divide the pivot row by the pivot value to make the pivot element 1
    tableau[pivot_row] = [x / pivot_value for x in tableau[pivot_row]]

    # Update the other rows
    for i in range(len(tableau)):
        if i != pivot_row:
            row_factor = tableau[i][pivot_col]
            tableau[i] = [tableau[i][j] - row_factor * tableau[pivot_row][j] for j in range(len(tableau[i]))]
    
    return tableau

# Example usage:
# A 2x2 Simplex tableau (3x3 in total with the objective row)
tableau = [
    [1, 2, 1, 4],
    [2, 1, 1, 5],
    [3, 2, 0, 6]  # Objective row
]

pivot_row = 1
pivot_col = 0
new_tableau = pivot_simplex(tableau, pivot_row, pivot_col)
print(new_tableau)
