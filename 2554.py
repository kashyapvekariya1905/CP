from itertools import combinations
from typing import List
banned = [1,6,5]
n = 5
maxSum = 6

banned = [1,2,3,4,5,6,7]
n = 8
maxSum = 1

banned = [11]
n = 7
maxSum = 50

def maxCount(banned: List[int], n: int, maxSum: int) -> int:
    lst = []
    for i in range(1,n+1):
        if i not in banned:
            lst.append(i)
    csum = 0
    count = 0
    for i in lst:
        if csum+i> maxSum:
            break
        csum+=i
        count+=1
    return count

print(maxCount(banned,n,maxSum))
