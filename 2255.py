words = ["a","b","c","ab","bc","abc"]
s = "abc"
words = ["a","a"]
s = "aa"

count = 0
for i in words:
    if s.startswith(i):
        count+=1
print(count)
