from typing import Counter, List


hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) %groupSize!=0:
        return False
    
    count = Counter(hand)
    minval = min(count.keys())

    while count:
        start_val = minval
        for i in range(start_val, start_val + groupSize):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                del count[i]
        minval = min(count.keys()) if count else float('inf')
    return True
print(isNStraightHand(hand,groupSize))