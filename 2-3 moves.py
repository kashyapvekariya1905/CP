def solve(n):
    if n == 1:
        return 2
    return (n+2)//3
t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))