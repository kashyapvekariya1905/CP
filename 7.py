x = 120
def reverse(x):
    # if x == 0:
    #     return 0
    # if x < 0:
    #     return -reverse(-x)
    # rev = 0
    # while x > 0:
    #     rev = (rev * 10) + (x % 10)
    #     x //= 10
    # return rev

    if x == 0:
        return 0
    neg = x<0
    x = abs(x)
    rev = int(str(x)[::-1])
    if neg:
        rev = -rev
    return rev
print(reverse(x))