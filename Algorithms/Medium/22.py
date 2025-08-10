def flatten_nested_list(l):
    result = []
    for i in l:
        if type(i) is list:
            for j in flatten_nested_list(i):
                result.append(j)
        else:
            result.append(i)
    return result


print(flatten_nested_list([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]
