from typing import List


class Solution:
    def __init__(self):
        self.my_grid = []

    def floodfill(self, grid, r, c, color):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 0:
            return
        grid[r][c] = color
        self.floodfill(grid, r - 1, c, color)
        self.floodfill(grid, r + 1, c, color)
        self.floodfill(grid, r, c - 1, color)
        self.floodfill(grid, r, c + 1, color)
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        max_color = 0
        self.my_grid = [[0 for i in range(n*3)] for j in range(n*3)]
        print(self.my_grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]=="/":
                    self.my_grid[i*3+0][j*3+2] = -1
                    self.my_grid[i*3+1][j*3+1] = -1
                    self.my_grid[i*3+2][j*3+0] = -1
                elif grid[i][j]=="\\":
                    self.my_grid[i*3+0][j*3+0] = -1
                    self.my_grid[i*3+1][j*3+1] = -1
                    self.my_grid[i*3+2][j*3+2] = -1
                    
        print(self.my_grid)
        for i in range(n*3):
            for j in range(n*3):
                if self.my_grid[i][j]==0:
                    max_color += 1
                    self.floodfill(self.my_grid, i, j, max_color)
        return max_color
grid = [" /","/ "]
print(Solution.regionsBySlashes(grid))
# Output: 2

grid = ["/\\","\\ "]
print(Solution.regionsBySlashes(grid))
# Output: 4

grid = ["//","/ "]
print(Solution.regionsBySlashes(grid))