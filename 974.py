from typing import List


nums = [4,5,0,-2,-3,1]
k = 5

def subarraysDivByK(nums: List[int], k: int) -> int:
    dict = {0:1}
    presum = 0
    rst = 0

    for i in nums:
        presum = (presum+i)%k
        if presum < 0:
            presum += k
        if presum in dict:
            rst += dict[presum]
        dict[presum] = dict.get(presum,0)+1
    return rst
print(subarraysDivByK(nums,k))