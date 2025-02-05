from typing import List
def checkSubarraySum(nums: List[int], k: int) -> bool:
    hmap = {0:-1}
    sum = 0
    for i,num in enumerate(nums):
        sum+=num
        if k!=0:
            sum %= k
        if sum in hmap:
            if i-hmap[sum]>1:
                return True
        else:
            hmap[sum] = i
    return False
        
nums = [23,2,4,6,7]
k = 6
print(checkSubarraySum(nums,k))