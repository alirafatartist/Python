def find_pivot(tableau):
    # Find entering variable (most negative value in the objective row)
    last_row = tableau[-1][:-1]
    pivot_col = min(range(len(last_row)), key=lambda i: last_row[i])

    # Find leaving variable by computing ratios (b_i / A_ij) for positive entries in pivot column
    ratios = []
    for i in range(len(tableau) - 1):
        if tableau[i][pivot_col] > 0:  # We can compute ratios only for positive entries
            ratios.append((tableau[i][-1] / tableau[i][pivot_col], i))
    if not ratios:
        raise ValueError("Unbounded solution")  # No positive values in pivot column
    
    # Find the minimum ratio to determine the pivot row
    pivot_row = min(ratios)[1]
    
    return pivot_row, pivot_col

# Example usage:
tableau = [
    [1, 2, 1, 4],
    [2, 1, 1, 5],
    [3, 2, 0, 6]  # Objective row
]
pivot_row, pivot_col = find_pivot(tableau)
print(f"Pivot Row: {pivot_row}, Pivot Column: {pivot_col}")
