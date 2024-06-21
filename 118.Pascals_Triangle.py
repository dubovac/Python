    array = [[1],[1,1]]
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return array

    b = array[1]

    for i in range(3, numRows + 1):
        a = []

        for j in range(1, i + 1):
            if j == 1 or j == i:
                a.append(1)
            else:
                a.append(b[j - 2] + b[j - 1])
        b = a

        array.append(a)

    return array

n = 30
a = generate(n)
print(a)
