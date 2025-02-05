from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    n, m = len(spells), len(potions)
    rst = []

    for spell in spells:
        count = 0
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if spell * potions[mid] >= success:
                right = mid - 1
            else:
                left = mid + 1
        count = m - left
        rst.append(count)

    return rst

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(spells,potions,success))