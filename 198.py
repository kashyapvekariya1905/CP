nums = [2,7,9,3,1]
# nums = [2,3,2]
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    rob, notr = nums[0], 0
    for i in range(1, len(nums)):
        rob, notr = notr + nums[i], max(rob, notr)
    return max(rob, notr)
print(rob(nums))