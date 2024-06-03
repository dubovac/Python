def searchInsert(nums, target):
    i = len(nums) // 2
    minimum = 0
    maximum = len(nums)

    if target <= nums[0]:
        return 0

    if target > nums[len(nums) - 1]:
        return len(nums)

    while nums[i] != target:
        if target < nums[i]:
            maximum = i
            i = (minimum + maximum) // 2
            if i == maximum:
                return i
        elif target > nums[i]:
            minimum = i
            i = (minimum + maximum) // 2
            if i == minimum:
                return i + 1
    return i
