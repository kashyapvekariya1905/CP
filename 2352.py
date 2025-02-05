grid = [[3,2,1],[1,7,6],[2,7,7]]

n = len(grid)
clm = []
for i in range(n):
    c = []
    for j in range(n):
        c.append(grid[j][i])
    clm.append(c)
count = 0
for i in grid:
    for j in clm:
        if i==j:
            count+=1
print(count)
