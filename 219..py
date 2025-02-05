from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    numMap = {}
    for i,num in enumerate(nums):
        if num in numMap and i-numMap[num]<=k:
            return True
        numMap[num] = i
    return False
# nums = [1,2,3,1]
# k = 3
nums = [1,0,1,1]
k = 1
# nums = [1,2,3,1,2,3]
# k = 2
print(containsNearbyDuplicate(nums,k))