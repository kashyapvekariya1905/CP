nums = [1,2,3,4,5]
k = 2
nums.sort()
nums = nums[::-1]
print(sum(nums[:k]))