import heapq
from typing import List


def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    minh = []
    maxh = []
    for i,j in zip(capital,profits):
        heapq.heappush(minh,(i,j))
    for _ in range(k):
        while minh and minh[0][0] <= w:
            c, p = heapq.heappop(minh)
            heapq.heappush(maxh, -p)
        if not maxh:
            break
        w += -heapq.heappop(maxh)
    return w

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(findMaximizedCapital(k,w,profits,capital))

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]
print(findMaximizedCapital(k,w,profits,capital))