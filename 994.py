from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    empty, fresh, rotten = 0,1,2
    m, n = len(grid), len(grid[0])
    q = deque()
    countFresh = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == rotten:
                q.append((i,j))
            if grid[i][j] == fresh:
                countFresh+=1
    
    if countFresh == 0:
        return 0
    
    minute = -1
    while q:
        qsize = len(q)
        minute+=1
        for _ in  range(qsize):
            i,j = q.popleft()
            for r,c in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                if 0<=r<m and 0<=c<n and grid[r][c] == fresh:
                    grid[r][c] = rotten
                    countFresh-=1
                    q.append((r,c))
    if countFresh==0:
        return minute
    return -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))
grid = [[0,2]]
print(orangesRotting(grid))