from typing import List


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for i in matrix:
        for j in i:
            if j == target:
                return True
    return False
            
print(searchMatrix(matrix,target))