def addDigits(num):
    if num > 9:
        while num > 9:
            s = 0

            while num != 0:
                s += num % 10;
                num //= 10

            num = s

    return num

x = 2147483647
print(f"{addDigits(x)}")
