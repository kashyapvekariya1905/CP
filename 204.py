def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    c = 0
    for i in range(n+1):
        if is_prime(i):
            c += 1
    return c

n = 10
print(generate_primes(n))
