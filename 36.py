from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:

    def validRow(row):
        s = set()
        for c in row:
            if c != ".":
                if c in s:
                    return False
                s.add(c)
        return True
    
    def validCol(col):
        s = set()
        for r in board:
            cell = r[col]
            if cell != ".":
                if cell in s:
                    return False
                s.add(cell)
        return True
    
    def valid(rs,cs):
        s= set()
        for i in range(rs, rs + 3):
            for j in range(cs, cs + 3):
                cell = board[i][j]
                if cell != ".":
                    if cell in s:
                        return False
                    s.add(cell)
        return True
    
    for i in range(9):
        if not validRow(board[i]) or not validCol(i):
            return False
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not valid(i,j):
                return False
    return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))


# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
