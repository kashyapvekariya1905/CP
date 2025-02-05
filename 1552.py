def maxDistance(position, m):
    position.sort()
    
    def canPlaceBalls(minf):
        count = 1  
        last = position[0]
        for i in range(1, len(position)):
            if position[i] - last >= minf:
                count += 1
                last = position[i]
                if count == m:
                    return True
        return False
    low, high = 1, position[-1] - position[0]
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if canPlaceBalls(mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best

position1 = [1, 2, 3, 4, 7]
m1 = 3
print(maxDistance(position1, m1))  # Output: 3

position2 = [5, 4, 3, 2, 1, 1000000000]
m2 = 2
print(maxDistance(position2, m2))  # Output: 999999999