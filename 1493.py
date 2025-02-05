nums = [0,1,1,1,0,1,1,0,1]
rst = 0
zero = 0
l = 0
n = len(nums)
for i in range(n):
    if nums[i] == 0:
        zero += 1
    while zero>1:
        if nums[l] == 0:
            zero-=1
        l+=1
    rst = max(rst,i-l)

print(rst)