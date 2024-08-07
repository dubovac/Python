# 766. Toeplitz Matrix
# Easy
# Topics
# Companies
# Hint
#
# Given an m x n matrix, return true if the matrix is Toeplitz.
# Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
#
#  
#
# Example 1:
#
#       Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
#       Output: true
#       Explanation:
#       In the above grid, the diagonals are:
#       "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
#       In each diagonal all elements are the same, so the answer is True.
#
# Example 2:
#
#       Input: matrix = [[1,2],[2,2]]
#       Output: false
#       Explanation:
#       The diagonal "[1, 2]" has different elements.
#
#  
#
# Constraints:
#
#       m == matrix.length
#       n == matrix[i].length
#       1 <= m, n <= 20
#       0 <= matrix[i][j] <= 99
#
#  
#
# Follow up:
#
#       What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
#       What if the matrix is so large that you can only load up a partial row into the memory at once?
def isToeplitzMatrix(matrix):
    if len(matrix) == 1 or len(matrix[0]) == 1:
        return True

    for i in range(len(matrix[0]) - 1):
        j = 1

        while j < len(matrix) and i + j < len(matrix[0]):
            if matrix[j][i + j] != matrix[j - 1][i + j - 1]:
                return False
            j += 1

    for k in range(len(matrix) - 1):
        l = 1

        while k + l < len(matrix) and l < len(matrix[0]):
            if matrix[k + l][l] != matrix[k + l - 1][l - 1]:
                return False
            l += 1

    return True

m = [[1, 2, 3, 4],
     [5, 1, 2, 3],
     [9, 5, 1, 2]
    ]

print("True") if isToeplitzMatrix(m) else print("False")
