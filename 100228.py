class Solution:
    def minOperations(self, k: int) -> int:
        if k<=2:
            return k-1
        n = 0
        total = 1
        while total < k:
            n += 1
            total += n
        return n - 1 if total == k else n
k = 3
sol = Solution()
print(sol.minOperations(k))