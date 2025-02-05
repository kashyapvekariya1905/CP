import heapq
from typing import Counter
nums = [1,2]
k = 2
count = Counter(nums)
heap = [(-f,i) for f,i in count.items()]
heapq.heapify(heap)
top_k = [heapq.heappop(heap)[1] for _ in range(k)]
return top_k
