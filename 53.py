nums = [-2,1,-3,4,-1,2,1,-5,4]
cs = nums[0]
ms = nums[0]
for i in nums[1:]:
    cs = max(i,cs+i)
    ms = max(cs,ms)
print(ms)