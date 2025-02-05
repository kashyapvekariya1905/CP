from typing import List
import heapq

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, i))
            adj[v].append((u, w, i))

        def dijkstra(src, replace_neg_one):
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                if u == destination:
                    break
                for v, w, i in adj[u]:
                    if w == -1:
                        w = 1 if not replace_neg_one else 2 * 10**9
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist[destination]

        shortest = dijkstra(source, False)
        if shortest < target:
            return []

        if shortest == target:
            return [[u, v, 1 if w == -1 else w] for u, v, w in edges]

        longest = dijkstra(source, True)
        if longest > target:
            return []

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue
            lo, hi = 1, 2 * 10**9
            while lo < hi:
                mid = (lo + hi) // 2
                edges[i][2] = mid
                if dijkstra(source, True) >= target:
                    hi = mid
                else:
                    lo = mid + 1
            edges[i][2] = lo

        if dijkstra(source, False) == target:
            return edges
        return []