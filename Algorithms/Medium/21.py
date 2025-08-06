def rotate_list(list,k):
    # n = len(list)
    # k = k % n  # Handle cases where k is greater than the length of the list
    return list[-k:] + list[:-k]




print(rotate_list([1, 2, 3, 4], 2))
print(rotate_list([10, 20, 30, 40, 50], 3))
print(rotate_list([10, 20, 30, 40, 50], 7))




# if the left side
def rotate_list_left(list,k):
    # n = len(list)
    # k = k % n  # Handle cases where k is greater than the length of the list
    return list[k:] + list[:k]




print(rotate_list_left([1, 2, 3, 4], 2))
print(rotate_list_left([10, 20, 30, 40, 50], 3))
print(rotate_list_left([10, 20, 30, 40, 50], 7))