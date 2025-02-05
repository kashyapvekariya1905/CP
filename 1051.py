from typing import List
heights = [1,1,4,2,1,3]
heights = [5,1,2,3,4]

def heightChecker(heights: List[int]) -> int:
    # count = 0
    # # if heights == heights.sort():
    # #     return 0
    # n = len(heights)
    # for i in range(n):
    #     for j in range(i,n):
    #         if heights[i] > heights[j]:
    #             heights[i], heights[j] = heights[j], heights[i]
    #             count+=1
    # return count+1
    count = 0
    ex = sorted(heights)
    for i in range(len(heights)):
        if heights[i]!=ex[i]:
            count+=1
    return count

print(heightChecker(heights))