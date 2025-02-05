from typing import List
import itertools
def combine(n: int, k: int) -> List[List[int]]:
    rst = []
    for i in range(n):
        rst.append(i+1)
    com = [list(i) for i in itertools.combinations(rst,k)]
    return com

n = 1
k = 1
print(combine(n,k))
# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]