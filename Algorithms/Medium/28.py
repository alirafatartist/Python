def find_missing_number(nums):
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1


nums = [1, 2, 4, 5, 6]
print(find_missing_number(nums))


def find_missing_number2(nums):
    for i in range(len(nums)):
        if nums[i+1] != nums[i]+1:
            return nums[i] + 1

nums = [1, 2, 4, 5, 6]
print(find_missing_number2(nums))

# def find_missing_number(nums):
#     n = len(nums) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum


# nums = [1, 2, 4, 5, 6]
# print(find_missing_number(nums))