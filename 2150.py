from typing import List


def findLonely(nums: List[int]) -> List[int]:
    rst = []
    temp = []
    occ = {}
    for i in nums:
        if i in occ:
            occ[i] += 1
        else:
            occ[i] = 1
    # print(occ)
    for i in occ:
        if occ[i] == 1:
            temp.append(i)
    for i in range(len(temp)):
        if ((temp[i]-1) in temp) or ((temp[i]+1) in temp):
            continue
        else:
            rst.append(temp[i])
    return rst
nums = [10,6,5,8]
nums = [1,3,5,3]
print(findLonely(nums))