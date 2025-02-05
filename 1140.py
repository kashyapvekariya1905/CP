from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
        dp = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for m in range(n, 0, -1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sums[i]
                else:
                    dp[i][m] = max(suffix_sums[i] - dp[i + x][max(m, x)] 
                                   for x in range(1, 2 * m + 1))
        return dp[0][1]