nums = [0]
# [1,3,12,0,0]
for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(i)
print(nums)