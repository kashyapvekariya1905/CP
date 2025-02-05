nums = [1,2,3,4]
k = 5
c = {}
op = 0
for i in nums:
    cmp = k - i
    if cmp in c and c[cmp] >0:
        op +=1
        c[cmp]-=1
        if c[cmp] == 0:
            del c[cmp]
    else:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
print(op)