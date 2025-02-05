def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes

def count_almost_primes(n):
    primes = sieve_of_eratosthenes(n)
    print(primes)
    almost_primes = 0
    for i in range(2, n + 1):
        divisors = set()
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                if primes[j]:
                    divisors.add(j)
                if i // j!= j and primes[i // j]:
                    divisors.add(i // j)
        if len(divisors) == 2:
            almost_primes += 1
    return almost_primes

n = int(input())
print(count_almost_primes(n))