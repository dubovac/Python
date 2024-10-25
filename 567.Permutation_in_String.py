# 567. Permutation in String
# Medium
# Topics
# Companies
# Hint
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
#  
#
# Example 1:
#
#       Input: s1 = "ab", s2 = "eidbaooo"
#       Output: true
#       Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
#
#       Input: s1 = "ab", s2 = "eidboaoo"
#       Output: false
#
#  
#
# Constraints:
#
#       1 <= s1.length, s2.length <= 10^4
#       s1 and s2 consist of lowercase English letters.

def checkInclusion(s1, s2):
    if len(s1) == 0:
        return True

    if len(s1) > len(s2):
        return False

    t1 = [0] * 26

    for i in range(len(s1)):
        t1[ord(s1[i]) - ord('a')] += 1

    for i in range(len(s2) - len(s1) + 1):
        t2 = [0] * 26

        for j in range(len(s1)):
            t2[ord(s2[i + j]) - ord('a')] += 1

        t = 1

        for j in range(26):
            if t1[j] != t2[j]:
                t = 0
                break

        if t:
            return True
    
    return False

s1 = "ab"
s2 = "eidbaooo"
print(f"{checkInclusion(s1, s2)}")
