from typing import List
nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
def findOccurrences(nums: List[int], queries: List[int], x: int) -> List[int]:
    occ = []
    for i,num in enumerate(nums):
        if num == x:
            occ.append(i)
    ans = []
    for k in queries:
        if k <= len(occ):
            ans.append(occ[k-1])
        else:
            ans.append(-1)
    return ans
print(findOccurrences(nums,queries,x))