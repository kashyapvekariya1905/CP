def isPowerOfTwo(n: int) -> bool:
    # while n%2 == 0:
    #     n = n//2
    # if n == 1:
    #     return True
    # return False

    if n <= 0:
        return False
    print(n & (n - 1))
    return (n & (n - 1)) == 0
n = 16
print(isPowerOfTwo(n))