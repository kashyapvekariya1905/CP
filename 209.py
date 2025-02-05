from typing import List

target = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]

def minSubArrayLen(target: int, nums: List[int]) -> int:
    rst = float('inf')
    st = 0
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            rst = min(rst,i-st+1)
            total -= nums[st]
            st +=1
    return rst if rst != float('inf') else 0
print(minSubArrayLen(target,nums))