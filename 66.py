from ast import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int(''.join(map(str,digits)))
        result += 1
        result2 = str(result)
        rst = []
        for char in result2:
            rst.append(int(char))
        return rst
    
sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([4,3,2,1]))