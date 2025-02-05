nums = [1,12,-5,-6,50,3]
k = 4
n = len(nums)
current_sum = sum(nums[:k])
max_sum = current_sum
for i in range(k, n):
    current_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, current_sum)
print(max_sum / k)