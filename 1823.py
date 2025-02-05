def findTheWinner(n: int, k: int) -> int:
    w = 0
    for i in range(1,n+1):
        w = (w + k) % i
    return w+1

n = 5
k = 2
print(findTheWinner(n,k))
n = 6
k =5
print(findTheWinner(n,k))