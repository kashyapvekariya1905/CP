height = [1,8,6,2,5,4,8,3,7]
l, r = 0,len(height)-1
rst = 0
while l < r:
    width = r-l
    if height[l]<height[r]:
        cr = height[l]*width
        l +=1
    else:
        cr = height[r]*width
        r-=1
    rst = max(rst,cr)
print(rst)