def maxlist(list):
    return max(list)


print(maxlist([1,2,3,4,5]))

def maxlist2(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j]<list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    
    return list[0]


print(maxlist2([6,3,9,3,4]))
