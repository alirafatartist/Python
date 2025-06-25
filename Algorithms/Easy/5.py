def ReverseList(list):
    result =[]

    for i in range(len(list)-1,-1,-1):
        result.append(list[i])

    return result


print(ReverseList([1, 2, 3, 4, 5]))
