from collections import Counter
from typing import List

def min_length(nums):
    count = 0
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 2
        else:
            count += 1
            i += 1
    return count

nums = [1, 1, 2, 2, 3, 3]
print(min_length(nums))
