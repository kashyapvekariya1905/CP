from math import ceil
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    def check(k):
        hour = 0
        for i in piles:
            hour+=ceil(i/k)
        return hour<=h
    l = 1
    r = max(piles)
    while l<r:
        k=(l+r)//2
        if check(k):
            r=k
        else:
            l=k+1
    return l

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))
piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles,h))
piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles,h))