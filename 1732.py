from typing import List
gain = [-4,-3,-2,-1,4,3,2]
def largestAltitude(gain: List[int]) -> int:
    c = 0
    ma = 0
    for ch in gain:
        c+=ch
        if c>ma:
            ma = c
    return ma
print(largestAltitude(gain))