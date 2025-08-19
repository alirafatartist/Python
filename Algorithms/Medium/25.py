def Remove_Duplicates(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result


def longest_consecutive_sequence(nums):
    nums = sorted(Remove_Duplicates(nums))  # Remove duplicates and sort
    counter = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            counter += 1

    return counter


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Output: 4 (The sequence is [1, 2, 3, 4])
print(longest_consecutive_sequence([0, -1, 1, 2, 3, 4]))    # Output: 6 (The sequence is [-1, 0, 1, 2, 3, 4])
print(longest_consecutive_sequence([1, 2, 0, 1]))            # Output: 3 (The sequence is [0, 1, 2])


