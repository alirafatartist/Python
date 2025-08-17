def calculate_Transportaion_costs(supply,demand,costsFW):
    k = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
    totalCost=0
    for i in range(len(supply)):
        for j in range(len(demand)):
            if supply[i] >= demand[j]:
                k[i][j] = demand[j]
                supply[i] = supply[i] - demand[j]
                demand[j] = 0
                totalCost += k[i][j] * costsFW[i][j]
            else:
                k[i][j] = supply[i]
                demand[j] = demand[j] - supply[i]
                supply[i] = 0
                totalCost += k[i][j] * costsFW[i][j]
            
    print('The transportaion Array is: ')
    for row in k:
        print(row)
    print('Total Cost is: ', totalCost)


supply = [50,60,120]
demand = [90,70,40,50]
costs_for_each_Factory_Warhouses = [[8,9,11,16],[12,7,5,8],[14,10,6,7]]
calculate_Transportaion_costs(supply,demand,costs_for_each_Factory_Warhouses)



# supply = [300,400,500]
# demand = [250,350,400]
# costs_for_each_Factory_Warhouses = [[3,1,7],[2,6,5],[8,3,3]]