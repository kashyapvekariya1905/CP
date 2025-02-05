from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        max_heap = [(-1.0, start)]
        visited = set()
        while max_heap:
            prob, node = heappop(max_heap)
            prob = -prob 
            if node == end:
                return prob
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, edge_prob in graph[node]:
                if neighbor not in visited:
                    new_prob = prob * edge_prob
                    heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0