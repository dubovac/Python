def getRow(rowIndex):
    if rowIndex == 0:
        return [1]

    current = [1, 1]
    
    if rowIndex == 1:
        return current

    for i in range(rowIndex + 2):
        a = []

        for j in range(1, i + 1):
            if j == 1 or j == i:
                a.append(1)
            else:
                a.append(current[j - 2] + current[j - 1])

        current = a

    return current

for i in range(35):
    rI = i
    a = getRow(rI)
    print(a)
