def square_list(list):
    result =[]
    for i in list:
        result.append(i**2)

    return result

print(square_list([1, 2, 3, 4, 5]))
# another solution
print([x**2 for x in [1,2,3,4,5]])