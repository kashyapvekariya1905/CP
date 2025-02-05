from typing import List
nums = [20,100,10,12,5,13]
def increasingTriplet(nums: List[int]) -> bool:
    rst = False
    for i in range(len(nums)-2):
        if nums[i]<nums[i+1]<nums[i+2]:
            rst = True
        else:
            rst = False
    return rst
print(increasingTriplet(nums))

# if len(nums) < 3:
#     return False

# first = float('inf')
# second = float('inf')

# for num in nums:
#     if num <= first:
#         first = num
#     elif num <= second:
#         second = num
#     else:
#         return True

# return False