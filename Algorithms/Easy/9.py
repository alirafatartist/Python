def multiply_list(list,multiplier):
    result =[]
    for i in list:
        result.append(i*multiplier)

    return result

print(multiply_list([1, 2, 3, 4, 5],2))
# Compare this snippet from Easy/6.py:
print([x * 2 for x in [1, 2, 3, 4, 5]])
