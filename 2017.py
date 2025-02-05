from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0][1:])
        bottom = 0
        rst = max(top,bottom)
        for i in range(len(grid[0])-1):
            top -= grid[0][i+1]
            bottom += grid[1][i]
            temp = max(top,bottom)
            if temp <= rst :
                rst = temp
            else:
                break
        return rst