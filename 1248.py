from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    count = 0
    p = 0
    pcount = {0:1}
    for i in nums:
        if i%2!=0:
            p += 1
        if p-k in pcount:
            count+=pcount[p-k]
        if p in pcount:
            pcount[p]+=1
        else:
            pcount[p] = 1
    return count

nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums,k))
nums = [2,4,6]
k = 1
print(numberOfSubarrays(nums,k))
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(numberOfSubarrays(nums,k))
