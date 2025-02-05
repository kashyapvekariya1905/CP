from typing import List
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1
        return True
class solution:
    def maxNumEdgesToRemove(self,n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        edges.sort(key=lambda x: x[0],reverse=True)
        use = 0
        for i,u,v in edges:
            u-=1
            v-=1
            if i == 3:
                use+=alice.union(u,v) | bob.union(u,v)
            elif i == 2:
                use+=bob.union(u,v)
            else:
                use+=alice.union(u,v)
        if alice.count>1 or bob.count>1:
            return-1
        return len(edges) - use

s = solution()
n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
print(s.maxNumEdgesToRemove(n,edges))
n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
print(s.maxNumEdgesToRemove(n,edges))
n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]
print(s.maxNumEdgesToRemove(n,edges))