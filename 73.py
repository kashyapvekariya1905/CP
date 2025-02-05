from typing import List
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
def setZeroes(matrix: List[List[int]]) -> None:
    zerop = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # print(matrix[i][j])
                zerop.append((i,j))
    for i,j in zerop:
        # matrix[i] = [0]*n
        for k in range(n):
            matrix[k][j] = 0
        for k in range(m):
            matrix[i][k] = 0
    print(zerop)
    print(matrix)
print(setZeroes(matrix))
# [[0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]]