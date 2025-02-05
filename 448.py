from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rst = []
        for i in range(n+1):
            if i not in nums:
                rst.append(i)
        rst.remove(0)
        return rst
    
nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
print(Solution().findDisappearedNumbers(nums))