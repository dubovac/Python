# 1207. Unique Number of Occurrences
# Easy
# Topics
# Companies
# Hint
#
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
#
#  
#
# Example 1:
#
#       Input: arr = [1,2,2,1,1,3]
#       Output: true
#       Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1.
#       No two values have the same number of occurrences.
#
# Example 2:
#
#       Input: arr = [1,2]
#       Output: false
#
# Example 3:
#
#       Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
#       Output: true
#
#  
#
# Constraints:
#
#       1 <= arr.length <= 1000
#       -1000 <= arr[i] <= 1000

def uniqueOccurrences(arr):
    m = {}

    for x in arr:
        if x not in m.keys():
            m[x] = 1
        else:
            m[x] += 1

    l = list(m.values())

    l.sort()

    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            return False

    return True


a = [1, 2, 3, 1, 1, 3]

l = uniqueOccurrences(a)

print(l)


a = [1, 2]

l = uniqueOccurrences(a)

print(l)

a = [-3,0,1,-3,1,1,1,-3,10,0]

l = uniqueOccurrences(a)

print(l)
