def check_if_sorted(list):
    return sorted(list) == list


print(check_if_sorted([1, 2, 3, 4]))  # True
print(check_if_sorted([4, 3, 2, 1]))  # False


# another solution
def check_if_sorted2(list):
    ref = list[:] #means no thing change if the list changed
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

    return list == ref


print(check_if_sorted2([1, 2, 3, 4]))  # True
print(check_if_sorted2([4, 3, 2, 1]))  # False