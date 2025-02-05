from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obset = set(map(tuple, obstacles))
        x = y = di = 0
        maxdsq = 0
        for i in commands:
            if i == -2:  
                di = (di - 1) % 4
            elif i == -1:  
                di = (di + 1) % 4
            else:
                for _ in range(i):
                    if (x + dx[di], y + dy[di]) not in obset:
                        x += dx[di]
                        y += dy[di]
                        maxdsq = max(maxdsq, x*x + y*y)
                    else:
                        break
        return maxdsq
solution = Solution()
print(solution.robotSim([4,-1,3], [])) 
print(solution.robotSim([4,-1,4,-2,4], [[2,4]]))  
print(solution.robotSim([6,-1,-1,6], [])) 