from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    maxw = 0
    zeors = 0
    n = len(nums)
    l = 0
    for r in range(n):
        if nums[r] == 0:
            zeors += 1
        while zeors > k:
            if nums[l] == 0:
                zeors -= 1
            l += 1
        w = r-l+1
        maxw = max(maxw,w)
    return maxw

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums,k))