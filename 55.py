from typing import List
nums = [3,2,1,0,4]
def canJump(nums: List[int]) -> bool:
    loc = 0
    for i in range(len(nums)):
        if i>loc:
            return False
        loc = max(loc,i+nums[i])
        if loc >= len(nums)-1:
            return True
    return False
print(canJump(nums))