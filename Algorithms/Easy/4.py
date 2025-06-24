def CountOccurrences(list,ele):
    count=0
    for i in list:
        if i == ele:
            count+=1

    return count

print(CountOccurrences([1, 2, 3, 2, 4, 2, 5],2)) # 3
