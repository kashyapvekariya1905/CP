from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    li = findLeft(nums, target)
    ri = findRight(nums, target)

    if li <= ri and ri < len(nums) and nums[li] == target and nums[ri] == target:
        return [li, ri]
    else:
        return [-1, -1]
    
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))