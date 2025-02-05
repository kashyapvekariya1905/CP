
def mergeAlternately(word1: str, word2: str) -> str:
    rst = ""
    l = max(len(word1),len(word2))
    for i in range(l):
        if i < len(word1):
            rst += word1[i]
        if i < len(word2):
            rst += word2[i]
    return rst


word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1,word2))