from typing import Counter, List


def minOperations(nums: List[int]) -> int:
    count = 0
    freq = Counter(nums)
    print(freq)
    for i in freq.values():
        if i < 2:
            return -1
        a = i//3
        rem = i%3

        if rem == 0:
            count+=a
        elif rem == 1:
            if a>=1:
                count+=a-1+2
            else:
                return -1
        elif rem ==2:
            count+=a+1
    return count
nums = [2,3,3,2,2,4,2,3,4]
nums = [2,1,2,2,3,3]
print(minOperations(nums))

