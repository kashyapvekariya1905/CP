arr = [2,3,1,6,7]
n = len(arr)
count = 0
a = [0]*(n+1)
for i in range(n):
    a[i+1] = a[i]^arr[i]
for i in range(n):
    for k in range(i+1,n):
        if a[i] == a[k+1]:
            count += (k-i)
print(count)