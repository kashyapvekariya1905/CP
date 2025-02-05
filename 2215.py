from typing import List
def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    n1 = set(nums1)
    n2 = set(nums2)
    ans = [[],[]]
    for i in n1:
        if i not in nums2:
            ans[0].append(i)
    for k in n2:
        if k not in nums1:
            ans[1].append(k)
    return ans
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))