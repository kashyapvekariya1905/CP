nums = [1,2,3,4,5,6,7]
k = 3
for i in range(k):
    temp = [nums.pop()]
    nums = temp + nums[:1]+ nums[1:]
print(nums)

n = len(nums)
k = k % n
nums.reverse()
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])