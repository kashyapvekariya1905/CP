from typing import List


def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    rowCols = {}
    rows = len(mat)
    cols = len(mat[0])
    arrLen = len(arr)
    for r in range(rows):
        for c in range(cols):
            rowCols[mat[r][c]] = [r,c]
    rzero = [0]*rows
    czero = [0]*cols
    for i in range(arrLen):
        num = arr[i]
        rzero[rowCols[num][0]] += 1
        czero[rowCols[num][1]] += 1
        
        if czero[rowCols[num][1]] == rows : return i
        elif rzero[rowCols[num][0]] == cols : return i

arr = [1,3,4,2]
mat = [[1,4],[2,3]]
print(firstCompleteIndex(arr,mat))