from typing import List
def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    n = len(customers)
    total = 0
    for i in range(n):
        if grumpy[i] == 0:
            total += customers[i]
    a = 0
    current = 0
    for i in range(minutes):
        if grumpy[i] == 1:
            current += customers[i]
    a = current
    for i in range(minutes, n):
        if grumpy[i] == 1:
            current += customers[i]
        if grumpy[i - minutes] == 1:
            current -= customers[i - minutes]
        a = max(a, current)
    return total + a

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(maxSatisfied(customers,grumpy,minutes))