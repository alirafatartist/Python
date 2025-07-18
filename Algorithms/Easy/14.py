def Remove_Duplicates(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result


print(Remove_Duplicates(["a", "b", "a", "c", "c"]))

# another solution

def Remove_Duplicates2(list):
    result = []
    for i in list:
        while i not in result:
            result.append(i)
    return result


print(Remove_Duplicates2(["a", "b", "a", "c", "c"]))