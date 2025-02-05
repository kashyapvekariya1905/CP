from typing import List
def minimumAverage(nums: List[int]) -> float:
    n = len(nums)
    nums.sort()
    avg=[]
    for i in range(int(n/2)):
        a = min(nums)
        b = max(nums)
        avg.append((a+b)/2)
        nums.remove(a)
        nums.remove(b)
    return min(avg)

nums = [7,8,3,4,15,13,4,1]
nums = [1,9,8,3,10,5]
nums = [1,2,3,7,8,9]


print(minimumAverage(nums))