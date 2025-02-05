import math


def maxHeightOfTriangle(red: int, blue: int) -> int:
    if red < blue:
        return maxHeightOfTriangle(blue, red)

    h1 = int(math.sqrt(4 * blue + 1))
    h2 = int(math.sqrt(blue)) * 2

    if ((h1 + 1) * (h1 + 1)) // 4 <= red:
        return h1
    if ((h2 + 1) * (h2 + 1) - 1) // 4 <= red:
        return h2
    if ((h1 - 1) * (h1 - 1)) // 4 <= red:
        return h1 - 1
    return h2 - 1