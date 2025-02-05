from typing import Counter
s = "abccccdd"
if len(s) == 1:
    print(1)
count = Counter(s)
print(count)
l = 0
odd = False
for i in count.values():
    if i%2==0:
        l+=i
    else:
        l+=i-1
        odd = True
if odd:
    l+=1
print(l)