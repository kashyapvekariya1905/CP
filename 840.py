from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check1(matrix):
            rsum = sum(matrix[0])
            for row in matrix:
                if sum(row) != rsum:
                    return False
            return True
        
        def check2(matrix):
            transposed = [list(row) for row in zip(*matrix)]
            return check1(transposed)
        
        def check3(matrix):
            n = len(matrix)
            d1 = sum(matrix[i][i] for i in range(n))
            d2 = sum(matrix[i][n-i-1] for i in range(n))
            return d1 == d2 and d1 == sum(matrix[0])
        
        def check(matrix):
            flattened = [num for row in matrix for num in row]
            if sorted(flattened) != list(range(1, 10)):
                return False
            return check1(matrix) and check2(matrix) and check3(matrix)
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [row[j:j+3] for row in grid[i:i+3]]
                if check(subgrid):
                    count += 1
        
        return count