def countDigitOne(n: int) -> int:
    # one = 0
    # for i in range(1, n + 1):
    #     numst = str(i)
    #     for dig in numst:
    #         if dig == '1':
    #             one += 1
    # return one
    one = 0
    f = 1
    while n//f>0:
        q = n//(f*10)
        r = n%(f*10)
        cd = r//f
        if cd>1:
            one+=(q+1)*f
        elif cd == 1:
            one+=q * f + r % f + 1
        else:
            one += q * f
        f *= 10
    return one
n = 13
print(countDigitOne(n))