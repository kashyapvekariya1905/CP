from typing import List
def minKBitFlips(nums: List[int], k: int) -> int:
    n = len(nums)
    flip = [0]*n
    count = 0
    rst = 0
    for i in range(n):
        if i>=k:
            count^=flip[i-k]
        if(nums[i]^count) == 0:
            if i+k>n:
                return -1
            rst +=1
            count^=1
            if i+k < n:
                flip[i] = 1
    return rst

nums = [0,1,0]
k = 1
# print(minKBitFlips(nums, k))

nums = [1,1,0]
k = 2
# print(minKBitFlips(nums, k))

nums = [0,0,0,1,0,1,1,0]
k = 3
print(minKBitFlips(nums, k))