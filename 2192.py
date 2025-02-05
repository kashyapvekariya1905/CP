from typing import List
from collections import defaultdict, deque
def getAncestors(n: int, edges: List[List[int]]) -> List[List[int]]:
    dc = defaultdict(list)
    ans = [[] for _ in range(n)]
    for x, y in edges:
        dc[x].append(y)
    def dfs(x, curr):
        for ch in dc[curr]:
            if ans[ch] and ans[ch][-1] == x: continue
            ans[ch].append(x)
            dfs(x, ch) 
    for i in range(n): dfs(i, i)
    return ans

    # graph = defaultdict(list)
    # for u,v in edges:
    #     graph[u].append(v)
    # ancs = [set() for _ in range(n)]
    # def dfs(node,anc):
    #     for i in graph[node]:
    #         if anc not in ancs[i]:
    #             ancs[i].add(anc)
    #             dfs(i,anc)
    # for node in range(n):
    #     dfs(node,node)
    # rst = [sorted(list(i)) for i in ancs]
    # return rst

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(getAncestors(n,edgeList))

n = 5
edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(getAncestors(n,edgeList))