citations = [3,0,6,1,5]
n = len(citations)
rst = 0
citations.sort(reverse=True)
for i,cit in enumerate(citations,start=1):
    if cit >= i:
        rst = i
    else:
        break
print(rst)