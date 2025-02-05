from typing import List
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
    # if target not in nums:
    #     return -1
    # l,r = 0,len(nums)-1
    # while l<r:
    #     m = (l+r)//2
    #     if nums[m] == target:
    #         return m
    #     if nums[l] <= nums[m]:
    #         if nums[l] <= target < nums[m]:
    #             r = m-1
    #         else:
    #             l = m+1
    #     else:
    #         if nums[m] < target <= nums[r]:
    #             l = m+1
    #         else:
    #             r = m-1
    # return l

nums = [4,5,6,7,0,1,2]
target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
# nums = [1]
# target = 0
print(search(nums,target))