class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0] * n for _ in range(n)]
        N_MAX = 10
        sol = []
        ans = []
        def printSolution(board):
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(board[i][j])
                    # print(" ", board[i][j], " ", end="")
                ans.append(row)
            sol.append(ans)
            # print()
            # print("--------------------")
        def isSafe(board, row, col):
            for i in range(col - 1, -1, -1):
                if board[row][i] == 1:
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            for i, j in zip(range(row, n), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False

            return True


        def solveNQueen(board, col):
            if col == n:
                printSolution(board)
                return True

            res = False
            for i in range(n):
                if isSafe(board, i, col):
                    board[i][col] = 1
                    res = solveNQueen(board, col + 1) or res  
                    board[i][col] = 0  
            return res
        solveNQueen(board, 0)
        return len(sol)
