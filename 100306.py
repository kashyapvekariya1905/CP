
def maxSumAfterQuery(nums, queries):
    MOD = 10**9 + 7
    max_sum = 0
    n = len(nums)
    dp = [0] * n

    for posi, xi in queries:
        nums[posi] = xi
        
        for i in range(n):
            if i == 0:
                dp[i] = max(0, nums[i])
            elif i == 1:
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        max_sum += max(dp) % MOD

    return max_sum % MOD

# Example usage:
nums1 = [3, 5, 9]
queries1 = [[1, -2], [0, -3]]
print(maxSumAfterQuery(nums1, queries1))  # Output: 21

nums2 = [0, -1]
queries2 = [[0, -5]]
print(maxSumAfterQuery(nums2, queries2))  # Output: 0
