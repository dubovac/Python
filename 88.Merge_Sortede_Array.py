def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    if n > 0:
        
        temp = []
        while m > 0 or n > 0:
            if m > 0 and n > 0:
                if nums1[0] <= nums2[0]:
                    temp.append(nums1.pop(0))
                    m -= 1
                else:
                    temp.append(nums2.pop(0))
                    n -= 1
            elif m == 0 and n > 0:
                temp.append(nums2.pop(0))
                n -= 1
            elif m > 0 and n == 0:
                temp.append(nums1.pop(0))
                m -= 1

        while len(nums1) > 0:
            nums1.pop()

        for x in temp:
            nums1.append(x)



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
print("[1, 2, 2, 3, 5, 6] - correct result\n")

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)
print("[1] - correct result\n")

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)
print("[1] - correct result\n")

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)
print("[1, 2] - correct result\n")

nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
m = 6
nums2 = [1, 2, 2]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
print("[-1, 0, 0, 1, 2, 2, 3, 3, 3] - correct result\n")
