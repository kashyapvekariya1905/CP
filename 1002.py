from typing import Counter


words = ["cool","lock","cook"]
# s = [set(i.lower()) for i in words]
# common = set.intersection(*s)
# rst = list(common)
# print(rst)

common = Counter(words[0])
for i in words[1:]:
    common&=Counter(i)
rst = list(common.elements())
print(rst)