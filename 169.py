from typing import List
def majorityElement(nums: List[int]) -> int:
    occ = {}
    majority_count = len(nums) // 2
    for i in nums:
        if i in occ:
            occ[i] += 1
        else:
            occ[i] = 1
        if occ[i] > majority_count:
            return i
    return -1

nums = [3,3,4]
print(majorityElement(nums))