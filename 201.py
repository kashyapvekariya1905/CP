left = 5
right = 7
rst = 0
while left < right :
    left >>=1
    right >>= 1
    rst +=1
print(left<<rst)