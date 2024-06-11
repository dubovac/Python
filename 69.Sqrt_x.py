def mySqrt(x):
    if x == 0:
        return 0
	
    i = 1
    
    while i * i <= x:
        i += 1

    return i - 1

x = 1000000
print(f"x = {x}")
print(f"sqrt({x}) = {mySqrt(x)}")

x = 9
print(f"x = {x}")
print(f"sqrt({x}) = {mySqrt(x)}")

x = 8
print(f"x = {x}")
print(f"sqrt({x}) = {mySqrt(x)}")

x = 100000000
print(f"x = {x}")
print(f"sqrt({x}) = {mySqrt(x)}")
