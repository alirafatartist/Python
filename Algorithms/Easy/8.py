def filter_odd_numbers(list):
    result =[]
    for i in list:
        if i % 2 != 0:
            result.append(i)

    return result


print(filter_odd_numbers([1, 2, 3, 4, 5]))