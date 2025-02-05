s = "zaz"
lst = []
rst = 0
for i in s:
    lst.append(ord(i))
for i in range(1,len(lst)):
    rst += abs(lst[i]-lst[i-1])
print(rst)