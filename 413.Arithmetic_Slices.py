# 413. Arithmetic Slices
# Medium
# Topics
# Companies
#
# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
#       For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
#
# Given an integer array nums, return the number of arithmetic subarrays of nums.
#
# A subarray is a contiguous subsequence of the array.
#
#  
#
# Example 1:
#
#       Input: nums = [1,2,3,4]
#       Output: 3
#       Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
#
# Example 2:
#
#       Input: nums = [1]
#       Output: 0
#
#  
#
# Constraints:
#
#       1 <= nums.length <= 5000
#       -1000 <= nums[i] <= 1000

def numberOfArithmeticSlices(nums):
    if len(nums) == 1 or len(nums) == 2:
        return 0

    result = 0

    i = 0

    while i < len(nums):
        diff = nums[i + 1] - nums[i]
        counter = 1
        i += 1

        while i + 1 < len(nums) and nums[i + 1] - nums[i] == diff:
            counter += 1
            i += 1

        if counter > 1:
            summa = 0

            for j in range(1, counter):
                summa += j

            result += summa

        if i == len(nums) - 1:
            i += 1

    return result

n = [1, 2, 3, 4]
print(f"n = {n}")
print(f"result: {numberOfArithmeticSlices(n)}\n")

n = [1]
print(f"n = {n}")
print(f"result: {numberOfArithmeticSlices(n)}\n")

n = [1, 2, 3, 4, 6]
print(f"n = {n}")
print(f"result: {numberOfArithmeticSlices(n)}\n")

n = [1, 2, 3, 4, 6, 8, 10]
print(f"n = {n}")
print(f"result: {numberOfArithmeticSlices(n)}\n")

n = [1, 2, 3, 4, 6, 8, 10, 11, 13, 15]
print(f"n = {n}")
print(f"result: {numberOfArithmeticSlices(n)}\n")
