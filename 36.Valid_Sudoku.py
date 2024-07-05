def isValidSudoku(board):
    compare = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(len(board)):
        result = [0] * 10
        for j in range(len(board[0])):
            if board[i][j] in compare:
                k = int(board[i][j])
                result[k] += 1
                if result[k] > 1:
                    return False

    for j in range(len(board)):
        result = [0] * 10
        for i in range(len(board[0])):
            if board[i][j] in compare:
                k = int(board[i][j])
                result[k] += 1
                if result[k] > 1:
                    return False

    for n in range(0, 7, 3):
        for m in range(0, 7, 3):
            result = [0] * 10
            for i in range(3):
                for j in range(3):
                    if board[n + i][m + j] in compare:
                        k = int(board[n + i][m + j])
                        result[k] += 1
                        if result[k] > 1:
                            return False

    return True

board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

print(True if isValidSudoku(board) else False)
