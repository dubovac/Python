# 1281. Subtract the Product and Sum of Digits of an Integer
# Easy
# Topics
# Companies
# Hint
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#
#  
#
# Example 1:
#
#       Input: n = 234
#       Output: 15 
#       Explanation: 
#       Product of digits = 2 * 3 * 4 = 24 
#       Sum of digits = 2 + 3 + 4 = 9 
#       Result = 24 - 9 = 15
#
# Example 2:
#
#       Input: n = 4421
#       Output: 21
#       Explanation: 
#       Product of digits = 4 * 4 * 2 * 1 = 32 
#       Sum of digits = 4 + 4 + 2 + 1 = 11 
#       Result = 32 - 11 = 21
#
#  
#
# Constraints:
#
#       1 <= n <= 10^5

def subtractProductAndSum(n):
    product = 1
    summa = 0
    num = 0

    while n > 0:
        num = n % 10
        product *= num
        summa += num
        n //= 10

    return product - summa

n = 234
print(f"n = {n}\tsubtractProductAndSum({n}) = {subtractProductAndSum(n)}")

n = 4421
print(f"n = {n}\tsubtractProductAndSum({n}) = {subtractProductAndSum(n)}")
