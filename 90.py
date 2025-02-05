nums = [4,4,4,1,4]
rst = []
n = len(nums)
rstlst = 2**n
for i in range(rstlst):
    s= []
    for j in range(n):
        if i &(1<<j):
            s.append(nums[j])
    rst.append(s)
unique = list(map(list, set(map(tuple, rst))))
print(unique)