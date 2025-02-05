# nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
occ={}
for i in nums:
    if i not in occ:
        occ[i] = 1
    else:
        occ[i] += 1
nums = []
for key,value in occ.items():
    if value >2:
        occ[key] = 2
    nums.append(key)
print(occ)
nums = [key for key, value in occ.items() for _ in range(value)]
print(nums)
print(len(nums))
