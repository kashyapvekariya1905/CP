import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    minheap = []
    for i in nums:
        if len(minheap)<k:
            heapq.heappush(minheap,i)
        else:
            heapq.heappushpop(minheap,i)
    return minheap[0]

    # nums.sort(reverse=True)
    # return nums[k-1]
nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums,k))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums,k))