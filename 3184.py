def countCompleteDayPairs(hours):
    r = [0] * 24
    for i in hours:
        r[i % 24] += 1
     
    count = 0
    count += (r[0] * (r[0] - 1)) // 2
    count += (r[12] * (r[12] - 1)) // 2
    
    for i in range(1, 12):
        count += r[i] * r[24 - i]
    
    return count

print(countCompleteDayPairs([12, 12, 30, 24, 24]))  
print(countCompleteDayPairs([72, 48, 24, 3]))  
