import math


def judgeSquareSum(c: int) -> bool:
    # for i in range(1,c):
    #     for j in range(i,c):
    #         if i**2 + j**2 == c:
    #             return True
    # return False
    for i in range(int(math.isqrt(c))+1):
        if math.isqrt(c-i**2) == math.sqrt(c-i**2):
            return True
    return False
c = 5
print(judgeSquareSum(c))
c = 3
print(judgeSquareSum(c))
c = 4
print(judgeSquareSum(c))