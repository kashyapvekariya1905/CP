word1 = "abc"
word2 = "bca"

def closeStrings(sword1: str, word2: str) -> bool:
    if len(word1)!=len(word2):
        return False
    f1 = {}
    f2 = {}
    for i in word1:
        if i in f1:
            f1[i]+=1
        else:
            f1[i] = 1
    for i in word2:
        if i in f2:
            f2[i]+=1
        else:
            f2[i] = 1
    if set(f1.keys()) != set(f2.keys()):
        return False
    if sorted(f1.values()) != sorted(f2.values()):
        return False
    return True
print(closeStrings(word1,word2))