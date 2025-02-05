n = 2147483645
lst = []
b = bin(n)
for i in b[2:]:
    lst.append(i)
occ = {}
for i in lst:
    if i not in occ:
        occ[i] = 1
    else:
        occ[i] += 1
print(occ['1'])
