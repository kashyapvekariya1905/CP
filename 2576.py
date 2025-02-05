from typing import List


def maxNumOfMarkedIndices(nums: List[int]) -> int:
    nums.sort()
    mark = 0
    n = len(nums)
    i,j = 0,n//2
    while i<n//2 and j<n:
        if 2*nums[i] <= nums[j]:
            mark+=2
            i+=1
        j+=1
    return mark
        

nums = [3,5,2,4]
# nums = [9,2,5,4]
# nums = [7,6,8]
nums = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40] 
print(maxNumOfMarkedIndices(nums))