def singleNumber(nums):
    x = nums[0]
    
    for i in range(1, len(nums)):
        x ^= nums[i]

    return x

nums = [4, 1, 2, 1, 2]
print(f"n = {singleNumber(nums)}")
