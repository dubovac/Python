# 383. Ransom Note
# Easy
# Topics
# Companies
#
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#  
#
# Example 1:
#
#       Input: ransomNote = "a", magazine = "b"
#       Output: false
#
# Example 2:
#
#       Input: ransomNote = "aa", magazine = "ab"
#       Output: false
#
# Example 3:
#
#       Input: ransomNote = "aa", magazine = "aab"
#   Output: true
#
#  
#
# Constraints:
#
#       1 <= ransomNote.length, magazine.length <= 10^5
#       ransomNote and magazine consist of lowercase English letters.
#

def canConstruct(ransomNote, magazine):
    rN = [0 for x in range(26)]
    m = [0 for x in range(26)]

    for x in ransomNote:
        rN[ord(x) - ord('a')] += 1

    for x in magazine:
        m[ord(x) - ord('a')] += 1

    for i in range(26):
        if rN[i] != 0 and rN[i] > m[i]:
            return False

    return True

ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(canConstruct(ransomNote, magazine))
