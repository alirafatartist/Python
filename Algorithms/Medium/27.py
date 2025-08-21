def Bubblesort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list),1):
            if list[i] > list[j]:
                temp= list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def merge_sorted_lists(list1,list2):
    result=[]
    for i in list1:
        result.append(i)
    
    for j in list2:
        result.append(j)

    return Bubblesort(result)



list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))



