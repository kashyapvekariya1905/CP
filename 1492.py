def get_factors(n,k):
    factors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    ans = factors[k-1]
    return ans
n = 7
k = 2
print(get_factors(n,k))
