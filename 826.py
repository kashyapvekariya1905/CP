from typing import List


def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    jbs = sorted(zip(difficulty,profit))
    mp = 0
    tp = 0
    j = 0
    n = len(jbs)
    worker.sort()
    for i in worker:
        while j < n and jbs[j][0]<=i:
            mp = max(mp,jbs[j][1])
            j+=1
        tp += mp
    return tp

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(maxProfitAssignment(difficulty,profit,worker))