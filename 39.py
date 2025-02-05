import itertools
from typing import List

candidates = [2, 3, 6, 7]
target = 7
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    rst = []
    s = []
    start = 0
    candidates.sort()
    def backtrack(start, target, s):
        if target == 0:
            rst.append(s[:])
            return 
        if target < 0:
            return 
        for i in range(start,len(candidates)):
            s.append(candidates[i])
            backtrack(i,target-candidates[i],s)
            s.pop()
    backtrack(0,target,[])
    return rst

print(combinationSum(candidates,target))