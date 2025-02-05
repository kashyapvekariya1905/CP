nums = [1,2,1,3,2,5]
occ = {}
rst = []
for num in nums:
    if num in occ:
        occ[num]+=1
    else:
        occ[num] = 1
for key,value in occ.items():
    if value == 1:
        rst.append(key)
print(rst)