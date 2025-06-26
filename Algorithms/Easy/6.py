def CheckforElement(list,ele):
    return ele in list


print(CheckforElement([1, 2, 3, 4, 5],7))


def check_for_element(my_list, element):
    for item in my_list:
        if item == element:
            return True
    return False

print(check_for_element([1, 2, 3, 4, 5],7))

