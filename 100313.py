from typing import List
def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    balls = [0] * (limit + 1)  # Initialize all balls as uncolored
    distinct_colors = 0
    result = []
    for ball, color in queries:
        if balls[ball] == 0:  # Ball is uncolored
            balls[ball] = color
            distinct_colors += 1
        elif balls[ball] != color:  # Ball is colored differently
            distinct_colors += 1
            balls[ball] = color
        result.append(distinct_colors)
    return result

limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
print(queryResults(limit,queries))



from typing import List

def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    balls = [0] * (limit + 1)
    colors = {}
    result = []

    for ball, color in queries:
        if balls[ball] != color:
            if balls[ball] in colors:
                colors[balls[ball]] -= 1
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1
            balls[ball] = color

        distinct_colors = sum(1 for count in colors.values() if count > 0)
        result.append(distinct_colors)

    return result

print(queryResults(1,[[0,1],[1,4],[1,1],[1,4],[1,1]]))