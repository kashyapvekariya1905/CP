from collections import deque
from typing import List
maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    row,col = len(maze),len(maze[0])
    queue = deque([(entrance[0], entrance[1], 0)])
    x = entrance[0]
    y = entrance[1]
    visited = set()
    visited.add((x,y))
    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r,c, step = queue.popleft()
        if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == row-1 or c == 0 or c == col-1):
            return step
        for dr,dc in dire:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and maze[nr][nc] == '.':
                visited.add((nr, nc))
                queue.append((nr, nc, step + 1))
    return -1

print(nearestExit(maze,entrance))