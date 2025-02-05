from functools import reduce
import operator
nums = [1,2,1,3]
occ = {}
for num in nums:
    if num in occ:
        occ[num]+=1
    else:
        occ[num] = 1
rstarr = []
for key,value in occ.items():
    if value == 2:
        rstarr.append(key)
xorall = reduce(operator.xor,rstarr)
print(xorall)