def minlist(list):
    return min(list)


print(minlist([1,2,3,4,5]))

def minlist2(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j]>list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    
    return list[0]


print(minlist2([6,3,9,3,4]))