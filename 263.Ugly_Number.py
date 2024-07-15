def isUgly(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        if n % 2 == 0:
            n /= 2
        if n % 3 == 0:
            n /= 3
        if n % 5 == 0:
            n /= 5

    if n == 1:
        return True

    return False

for i in range(1, 1000001):
    if isUgly(i):
        print(f"{i}:\t{'True' if isUgly(i) else 'False'}")
