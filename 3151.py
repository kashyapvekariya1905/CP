from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i=0
        a = True
        if len(nums)==1:
            return True
        else:
            while i < len(nums)-1:
                if (nums[i]%2) == (nums[i+1]%2):
                    a = False
                    break
                i+=1
            if a:
                return True
            else:
                return False
s = Solution()
arr = [2,1,4]
arr2 = [4,3,1,6]
print(s.isArraySpecial(arr2))