# 54. Spiral Matrix
# Medium
# Topics
# Companies
# Hint
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
#
# Example 1:
#
#       1 → 2 → 3
#	            ↓
#       4 → 5   6
#       ↑	    ↓
#       7 ← 8 ← 9
#
#       Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#       Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
#
#       1 →  2 →  3 →  4
#                      ↓
#       5 →  6 →  7    8
#       ↑              ↓
#       9 ← 10 ← 11 ← 12
#
#       Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#       Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#       m == matrix.length
#       n == matrix[i].length
#       1 <= m, n <= 10
#       -100 <= matrix[i][j] <= 100
#/

def spiralOrder(matrix):
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)

    k = 0
    result = []
    rl = right * bottom                     # rl - result length

    while (True):
        for j in range(left, right):
            result.append(matrix[top][j])
            k += 1
            if k == rl:
                break

        if k == rl:
            break

        for i in range(top + 1, bottom):
            result.append(matrix[i][right - 1])
            k += 1
            if k == rl:
                break

        if k == rl:
            break

        for j in range(right - 2, left - 1, -1):
            result.append(matrix[bottom - 1][j])
            k += 1
            if k == rl:
                break

        if k == rl:
            break

        for i in range(bottom - 2, top, -1):
            result.append(matrix[i][left])
            k += 1
            if k == rl:
                break

        if k == rl:
            break
        
        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return result


m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

r = spiralOrder(m)
print(m)
print(r)
print()

m = [
        [1]
    ]

r = spiralOrder(m)
print(m)
print(r)
print()

m = [
        [ 1,  2,  3,  4,  5,  6,  7,  8],
        [ 9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30, 31, 32],
        [33, 34, 35, 36, 37, 38, 39, 40]
    ]

r = spiralOrder(m)
print(m)
print(r)
print()
