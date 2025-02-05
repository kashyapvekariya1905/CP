from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for k in range(n):
        matrix[k].reverse()


    # matrix = temp
    # print(matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)