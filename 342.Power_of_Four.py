# 342. Power of Four
# Easy
# Topics
# Companies
#
# Given an integer n, return true if it is a power of four. 
# Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#
#  
#
# Example 1:
#
#       Input: n = 16
#       Output: true
#
# Example 2:
#
#       Input: n = 5
#       Output: false
#
# Example 3:
#
#       Input: n = 1
#       Output: true
#
#  
#
# Constraints:
#
#       -2^31 <= n <= 2^31 - 1
#
#  
# Follow up: Could you solve it without loops/recursion?

import math

def isPowerOfFour(n):
    if n <= 0:
        return False

    return True if int(math.log(n) / math.log(4)) == math.log(n) / math.log(4) else False

n = 16
print(isPowerOfFour(n))

n = 5
print(isPowerOfFour(n))

n = -2147483648
print(isPowerOfFour(n))

n = 2
print(isPowerOfFour(n))
