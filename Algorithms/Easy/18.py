def sum_of_even_numbers(list):
    result = 0
    for i in list:
        if i % 2 ==0:
            result+=i

    return result


print(sum_of_even_numbers([1,2,3,5,4,6]))


# another slotution

def sum_of_even_numbers2(list):
    return sum(x for x in list if x % 2 == 0)


print(sum_of_even_numbers2([1,2,3,5,4,6]))