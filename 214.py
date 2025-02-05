s = "abcd"
# s = "aacecaaa"
def shortestPalindrome(s: str) -> str:
    # if s==s[::-1]:
    #     return s
    # else:
    #     l,r = 0,len(s)-1
    #     mid = (l+r)//2
    #     print(mid)
    #     if mid%2!=0:
    #         p1 = s[:mid]
    #         p1 = p1[::-1]
    #         p2 = s[mid+1:]
    #         print(p2)
    #         if len(p1) < len(p2):
    #             shorter, longer = p1, p2
    #         else:
    #             shorter, longer = p2, p1
    #         for char in longer[len(shorter):]:
    #             shorter += char
    #         shorter = shorter[::-1]
    #         rst = shorter+s[mid]+longer
    #         print(shorter,longer)
    #         return rst
    #     else:
    #         p = l+1
    #         p1 = s[p:]
    #         p2 = p1[::-1]
    #         rst = p2+s
    #         return rst  

    if not s:
        return s
    rev = s[::-1]
    for i in range(len(s)):
        if s.startswith(rev[i:]):
            return rev[:i]+s    
print(shortestPalindrome(s))