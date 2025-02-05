s = "leet**cod*e"
a = []
for i in s:
    if i == '*':
        a.pop()
    else:
        a.append(i)
print(''.join(a))
