from typing import List
def minPatches(nums: List[int], n: int) -> int:
    pat = 0
    miss = 1
    i = 0
    while miss<=n:
        if i < len(nums) and nums[i] <= miss:
            miss+=nums[i]
            i+=1
        else:
            miss+=miss
            pat+=1
    return pat

nums = [1,3]
n = 6
print(minPatches(nums,n))

nums = [1,5,10]
n = 20
print(minPatches(nums,n))