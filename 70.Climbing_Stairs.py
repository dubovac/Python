def climbStairs(n):
    first = 0
    second = 1
    third = 0

    for i in range(n):
        third = second + first
        first = second
        second = third

    return third

for i in range(1, 46):
    print(f"{i}:\t{climbStairs(i)}")
