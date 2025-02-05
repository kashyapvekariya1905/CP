from typing import List
nums = [5,2,6,1]

def countSmaller(nums: List[int]) -> List[int]:
    def mergeSort(arr,count):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = mergeSort(arr[:mid], count)
        right = mergeSort(arr[mid:], count)
        return merge(left, right)
    def merge(l,r):
        merged = []
        i, j = 0, 0
        while i < len(l) or j < len(r):
            if j == len(r) or (i < len(l) and l[i][1] <= r[j][1]):
                merged.append(l[i])
                counts[l[i][0]] += j
                i += 1
            else:
                merged.append(r[j])
                j += 1
        return merged
    counts = [0] * len(nums)
    indexed_nums = list(enumerate(nums))
    mergeSort(indexed_nums, counts)
    return counts
    # count = []
    # if len(nums) == 1:
    #     return [0]
    # for i in range(len(nums)):
    #     current = 0
    #     for j in range(i+1,len(nums)):
    #         if nums[i]>nums[j]:
    #             current +=1
    #     count.append(current)
    # return count

print(countSmaller(nums))