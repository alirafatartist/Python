def product_of_odd_numbers(list):
    result =1
    for i in list:
        if i % 2 != 0:
            result*=i
    return result


print(product_of_odd_numbers([1, 2, 3, 4]))  # 3