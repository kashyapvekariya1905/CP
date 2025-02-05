def isSubsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    if not s:
        return True
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i +=1
            if i == len(s):
                return True
        j+=1
    return False

s = "axc"
t = "ahbgdc"
print(isSubsequence(s,t))