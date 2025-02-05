flowerbed = [1,0,0,0,1] 
n = 1
# true
# flowerbed = [1,0,0,0,1]
# n = 2
# false

count = 0
i = 0
while i < len(flowerbed):
    if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
        flowerbed[i] = 1
        count += 1
    i += 1
print(count >= n)