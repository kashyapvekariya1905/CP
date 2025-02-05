from typing import List
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    rst = []
    for i in range(len(candies)):
        if candies[i]+extraCandies>= max(candies):
            rst.append(True)
        else:
            rst.append(False)
    return rst



candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies,extraCandies))
