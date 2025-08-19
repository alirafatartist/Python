def calculate_transportation_costs(supply, demand, costsFW):
    totalCost = 0
    m = len(supply)
    n = len(demand)
    k = [[0 for _ in range(n)] for _ in range(m)]

    while True:
        min_cost = float('inf')
        row = -1
        col = -1

        # Find the least cost cell
        for i in range(m):
            for j in range(n):
                if supply[i] > 0 and demand[j] > 0 and costsFW[i][j] < min_cost:
                    min_cost = costsFW[i][j]
                    row = i
                    col = j

        if row == -1 or col == -1:
            break  # done allocating

        # Allocate as much as possible
        amount = min(supply[row], demand[col])
        k[row][col] = amount
        totalCost += amount * costsFW[row][col]
        supply[row] -= amount
        demand[col] -= amount

    print('The transportation array is:')
    for row in k:
        print(row)
    print('Total Cost is:', totalCost)




supply = [50, 60, 120]
demand = [90, 70, 40, 50]
costs = [
    [8, 9, 11, 16],
    [12, 7, 5, 8],
    [14, 10, 6, 7]
]

calculate_transportation_costs(supply, demand, costs)
