n = int(input())
a = 0
d = 0
s = input().upper()
def check(s):
    for i in s:
        if i == "A" or i == "D" : 
            if len(s) == n:
                return s
check(s)
for char in s :
    if char == "A" :
        a += 1
    elif char == "D" :
        d += 1

for j in range(len(s)):
    if a > d:
        print("Anton")
        break
    elif a < d:
        print("Danik")
        break
    else:
        print("Friendship")
        break