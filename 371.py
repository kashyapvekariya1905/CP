a = 2
b = 3

while b!= 0:
    c = a & b
    a = a ^ b
    b = c << 1
    print(c,a,b)
print(a)