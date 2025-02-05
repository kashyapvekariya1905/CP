from typing import List


def differenceOfSum(nums: List[int]) -> int:
    total = sum(nums)
    digits = 0
    for i in nums:
        digits += sum([int(j) for j in str(i)])
    return abs(total-digits)
nums = [1,15,6,3]
nums = [1,2,3,4]
print(differenceOfSum(nums))