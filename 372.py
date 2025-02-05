from typing import List
a = 2
b = [1,0]
a = 2147483647
b = [2,0,0]
# num = ""
# for i in b:
#     num += str(i)
# bint = int(num)
# rst = a**bint
# print(rst)
def superPow(a: int, b: List[int]) -> int:
    mod = 1337
    def modExp(b,e,m):
        rst = 1
        b = b%mod
        while e>0:
            if e%2==1:
                rst = (rst * b) % mod
            e = e>>1
            b = (b*b)%mod
        return rst
    def superMod(a,b,m):
        if not b :
            return 1
        last = b.pop()
        p1 = modExp(a,last,mod)
        p2 = modExp(superMod(a,b,mod),10,mod)
        return (p1 * p2) % mod
        
    return superMod(a, b, mod)
print(superPow(a,b))

