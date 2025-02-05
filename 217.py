from typing import List
occ = {}
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if num in occ:
                occ[num]+=1
            else:
                occ[num] = 1

        for key,value in occ.items():
            if value >=2:
                return True
        return False
            
sol = Solution()
nums = [2,14,18,22,22]
print(sol.containsDuplicate(nums))