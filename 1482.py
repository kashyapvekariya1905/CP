from typing import List


def minDays(bloomDay: List[int], m: int, k: int) -> int:
    if len(bloomDay) < m*k:
        return -1
    def able(day):
        bouquets = f = 0
        for i in bloomDay:
            if i <= day:
                f += 1
                if f == k:
                    bouquets += 1
                    f = 0
            else:
                f = 0
        return bouquets >= m
    l, r = 1, max(bloomDay)
    while l < r:
        mid = (l + r) // 2
        if able(mid):
            r = mid
        else:
            l = mid + 1
    return l if able(l) else -1

bloomDay = [1,10,3,10,2]
m = 3 
k = 1
print(minDays(bloomDay,m,k))

bloomDay = [1,10,3,10,2]
m = 3
k = 2
print(minDays(bloomDay,m,k))

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print(minDays(bloomDay,m,k))