# 896. Monotonic Array
# Easy
# Topics
# Companies
#
# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
#
#  
#
# Example 1:
#
#       Input: nums = [1,2,2,3]
#       Output: true
#
# Example 2:
#
#       Input: nums = [6,5,4,4]
#       Output: true
#
# Example 3:
#
#       Input: nums = [1,3,2]
#       Output: false
#
#  
#
# Constraints:
#
#       1 <= nums.length <= 10^5
#       -10^5 <= nums[i] <= 10^5

def isMonotonic(nums):
    incr = 0
    decr = 0

    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            incr = 1
        if nums[i + 1] < nums[i]:
            decr = 1
        if incr == 1 and decr == 1:
            return False

    return True

a = [1, 2, 2, 3]
print(isMonotonic(a))

b = [6, 5, 4, 4]
print(isMonotonic(b))

c = [1, 3, 2]
print(isMonotonic(c))

d = [4, 4, 4, 4]
print(isMonotonic(d))
