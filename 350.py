from typing import Counter, List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    count = Counter(nums1)
    rst = []
    for i in nums2:
        if count[i]>0:
            rst.append(i)
            count[i] -= 1
    return rst
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))