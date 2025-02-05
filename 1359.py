n = 3
def countOrders(n: int) -> int:
    mod = 10**9 +7
    if n == 0:
        return 1
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1] * i * (2*i - 1)%mod
    return dp[n]
print(countOrders(n))