n = int(input())
s = (5**n)%100000000000000
s1 = str(s)
s2 = s1[:-3:-1]
print(s2[::-1])