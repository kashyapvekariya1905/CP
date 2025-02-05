from collections import deque
from typing import List

def longestSubarray(nums: List[int], limit: int) -> int:
    maxdq = deque()
    mindq = deque()
    l = 0
    rst = 0
    n = len(nums)

    for i in range(n):
        while maxdq and nums[maxdq[-1]] < nums[i]:
            maxdq.pop()
        maxdq.append(i)
        while mindq and nums[mindq[-1]] > nums[i]:
            mindq.pop()
        mindq.append(i)
        while nums[maxdq[0]] - nums[mindq[0]] > limit:
            l += 1
            if maxdq[0] < l:
                maxdq.popleft()
            if mindq[0] < l:
                mindq.popleft()
        
        rst = max(rst, i - l + 1)
    
    return rst

nums = [8,2,4,7]
limit = 4
print(longestSubarray(nums,limit))
nums = [10,1,2,4,7,2]
limit = 5
print(longestSubarray(nums,limit))
nums = [4,2,2,2,4,4,2,2]
limit = 0
print(longestSubarray(nums,limit))