def isIsomorphic(s, t):
    s_array = [0] * len(s)
    t_array = [0] * len(t)

    s_counter = 0
    t_counter = 0
    return_bool = True

    for i in range(1, len(s)):
        s_check = True
        t_check = True

        for j in range(i):
            if s[i] == s[j]:
                s_array[i] = s_array[j]
                s_check = False
                break

        for j in range(i):
            if t[i] == t[j]:
                t_array[i] = t_array[j]
                t_check = False
                break

        if s_check:
            s_counter += 1
            s_array[i] = s_counter

        if t_check:
            t_counter += 1
            t_array[i] = t_counter

        if s_array[i] != t_array[i]:
            return_bool = False
            break

    return return_bool

s = "egg"
t = "add"
print(isIsomorphic(s, t))

s = "foo"
t = "bar"
print(isIsomorphic(s, t))

s = "paper"
t = "title"
print(isIsomorphic(s, t))
