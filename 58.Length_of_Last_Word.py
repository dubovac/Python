def lengthOfLastWord(s):
    w = s.split()
    return len(w[len(w) - 1])

test = "The quick brown fox jumps over the lazy dog."
print(lengthOfLastWord(test))

test = "   fly me   to   the moon  "
print(lengthOfLastWord(test))
