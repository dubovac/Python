def isPalindrome(s):
    if len(s) <= 1:
        return True

    s = s.lower()
    
    ss = ""
    for x in s:
        if x.isalnum():
            ss += x

    i = 0
    result = True

    while i <= len(ss) - 1 - i:
        if ss[i] != ss[len(ss) - 1 - i]:
            result = False
            break
        i += 1

    return result

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

s = "race a car"
print(isPalindrome(s))

s = " "
print(isPalindrome(s))

s = "p0"
print(isPalindrome(s))

s = "a."
print(isPalindrome(s))
