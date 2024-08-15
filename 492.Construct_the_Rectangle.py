# 492. Construct the Rectangle
# Easy
# Topics
# Companies
# Hint
#
# A web developer needs to know how to design a web page's size.
# So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
#
#       The area of the rectangular web page you designed must equal to the given target area.
#       The width W should not be larger than the length L, which means L >= W.
#       The difference between length L and width W should be as small as possible.
#
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
#
#  
#
# Example 1:
#
#       Input: area = 4
#       Output: [2,2]
#       Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
#       But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2].
#       So the length L is 2, and the width W is 2.
#
# Example 2:
#
#       Input: area = 37
#       Output: [37,1]
#
# Example 3:
#
#       Input: area = 122122
#       Output: [427,286]
#
#  
#
# Constraints:
#
#       1 <= area <= 10^7

def constructRectangle(area):
    result = []

    length = area
    width = 1
    l = area

    while l > width:
        if area % l == 0:
            width = area // l
            length = l
        
        l -= 1
    
    result.append(length)
    result.append(width)

    return result

a0 = 4
r0 = constructRectangle(a0)
print(f"{a0 = }\nlength[0] = {r0[0]}\twidth[0] = {r0[1]}\n")

a1 = 37
r1 = constructRectangle(a1)
print(f"{a1 = }\nlength[1] = {r1[0]}\twidth[1] = {r1[1]}\n")

a2 = 122122
r2 = constructRectangle(a2)
print(f"{a2 = }\nlength[2] = {r2[0]}\twidth[2] = {r2[1]}\n")

a3 = 40000
r3 = constructRectangle(a3)
print(f"{a3 = }\nlength[3] = {r3[0]}\twidth[3] = {r3[1]}\n")
