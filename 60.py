import itertools
from math import factorial


n = 9
k = 161191
digits = list(range(1,n+1))
rst = []
k-=1

for i in range(n,0,-1):
    f = factorial(i-1)
    ind = k//f
    rst.append(str(digits[ind]))
    digits.pop(ind)
    k%=f
print(''.join(rst))



# lst = []
# for i in range(1,n+1):
#     lst.append(i)
# p = list(itertools.permutations(lst))
# permutations = [list(p) for p in p]
# rst = [''.join(map(str, perm)) for perm in permutations]
# print(rst[k-1])