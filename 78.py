import itertools
arr = [1,2,3]
sub = []
for i in range(len(arr)+1):
    sub.extend(itertools.combinations(arr,i))
rst = [list(j) for j in sub]
print(rst)