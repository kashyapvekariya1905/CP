import itertools
from typing import List

nums = [1,1,5]
def nextPermutation(nums: List[int]):
    rst = list(itertools.permutations(nums))
    lst = [''.join(map(str, perm)) for perm in rst]
    lst.reverse()
    # if ''.join(map(str, nums)) in lst:
    #     ind = lst.index(''.join(map(str, nums)))
    #     nums = list(map(int, list(lst[(ind + 1) % len(lst)])))
    # return nums

    if nums in lst:
        ind = lst.index(nums)
        nums = lst[(ind+1)%len(lst)]
    return nums
print(nextPermutation(nums))