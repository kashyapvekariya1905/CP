s = ["h","e","l","l","o"]
# s = ["H","a","n","n","a","h"]

l,r = 0,len(s)-1
while l < r:
    s[l],s[r] = s[r], s[l]
    l+=1
    r-=1
print(s)