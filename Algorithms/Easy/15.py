def common_elements(list1,list2):
    result =[]
    for i in list1:
        if i in list2:
            result.append(i)

    return result

print(common_elements([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))




def commonElemenst(list1,list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result

print(commonElemenst([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))