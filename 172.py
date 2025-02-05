n = 5
def trailingZeroes(n: int) -> int:
    zeros = 0
    def fact(n):
        if n == 0:
            return 1
        return n*fact(n-1)
    a = fact(n)
    while a%10 == 0:
        zeros += 1
        a = a//10
    return zeros
print(trailingZeroes(n))