def lengthOfLongestSubstring(s: str) -> int:
    def check(s):
        unique = set(s)
        return len(unique) == 1
    if check(s):
        return 1
    n = len(s)
    if n == 0:
        return 0
    ci = {}
    ml = 0
    srt = 0
    for i in range(n):
        if s[i] in ci:
            srt = max(srt,ci[s[i]]+1)
        ci[s[i]] = i
        ml = max(ml,i-srt+1)
    return ml

print(lengthOfLongestSubstring('abcabcbb'))
# print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))