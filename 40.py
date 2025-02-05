from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()

    candidates.sort()
    result = []
    backtrack(0, target, [])
    return result

candidates = [10,1,2,7,6,1,5]
target = 8

print(combinationSum2(candidates, target))