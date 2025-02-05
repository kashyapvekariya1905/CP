def checkRecord(n: int) -> int:
    MOD = 10**9 + 7
    if n == 0:
        return 0
    
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(2):
            for k in range(3):
                dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                if j > 0:
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j-1][k]) % MOD
                if k > 0:
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
    result = 0
    for j in range(2):
        for k in range(3):
            result = (result + dp[n][j][k]) % MOD
    return result

print(checkRecord(2))    # Output: 8
print(checkRecord(1))    # Output: 3
print(checkRecord(10101)) # Output: 183236316
