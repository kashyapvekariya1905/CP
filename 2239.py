from typing import List


def findClosestNumber(nums: List[int]) -> int:
    clst = nums[0]
    mind = abs(nums[0])
    for i in nums:
        dst = abs(i)
        if dst<mind or (dst==mind and i>clst):
            clst = i
            mind = dst
    return clst

nums = [-4,-2,1,4,8]
print(findClosestNumber(nums))
nums = [2,-1,1]