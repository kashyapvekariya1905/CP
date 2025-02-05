s = "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join(s.lower() for char in s if char.isalnum())
        s = ''.join(char for char in s.lower() if char.isalnum())
        return s==s[::-1]
sol = Solution()
print(sol.isPalindrome(s))