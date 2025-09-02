def rotate_nested_list(nested_list, k):
    # تأكد أن k ضمن حدود الطول
    # k = k % len(nested_list)

    # التدوير باستخدام التقطيع
    return nested_list[-k:] + nested_list[:-k]


nested_list = [[1, 2], [3, 4, 5], [6]]
k = 1

print(rotate_nested_list(nested_list, k))
# Output: [[6], [1, 2], [3, 4, 5]]


nested_list = [[1, 2], [3, 4], [5], [6]]
k = 2
print(rotate_nested_list(nested_list, k))
# النتيجة: [[5], [6], [1, 2], [3, 4]]
