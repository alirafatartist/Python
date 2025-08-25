def create_simplex_tableau(c, A, b):
    """
    c: Coefficients of the objective function
    A: Coefficient matrix of constraints
    b: Right-hand side values of constraints
    """

    # Append the right-hand side to the coefficient matrix A
    augmented_matrix = [row + [b_val] for row, b_val in zip(A, b)]

    # Append the objective function as the last row
    objective_row = [-coef for coef in c]  # For maximization, negate the objective
    objective_row.append(0)  # Right-hand side of objective function (usually 0)
    augmented_matrix.append(objective_row)

    return augmented_matrix

# Example usage:
c = [3, 2]  # Objective function coefficients (maximize 3x + 2y)
A = [
    [1, 2],  # Constraints: x + 2y <= 4
    [3, 1]   # 3x + y <= 5
]
b = [4, 5]  # Right-hand side of constraints

tableau = create_simplex_tableau(c, A, b)
for row in tableau:
    print(row)

# Output:
# [1, 2, 4]
# [3, 1, 5]
# [-3, -2, 0]
