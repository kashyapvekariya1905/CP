str1 = "ABCABC"
str2 = "ABC"
s1 = set(str1)
s2 = set(str2)
inter = s1.intersection(s2)
rst = ''.join(inter)
print(rst)
