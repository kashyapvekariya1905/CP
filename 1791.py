from typing import List


def findCenter(edges: List[List[int]]) -> int:
    if edges[0][0] in edges[1]:
        return edges[0][0]
    else:
        return edges[0][1]

edges = [[1,2],[2,3],[4,2]]
# edges = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges))