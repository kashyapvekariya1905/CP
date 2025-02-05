from typing import List
def minIncrementForUnique(nums: List[int]) -> int:
    count = 0
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] <= nums[i-1]:
            inc = nums[i-1]+1-nums[i]
            nums[i] = nums[i-1]+1
            count += inc
    return count

nums = [1,2,2]
nums = [3,2,1,2,1,7]

print(minIncrementForUnique(nums))