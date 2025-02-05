def getLucky(s: str, k: int) -> int:
    def dsum(s2):
        return sum(int(i) for i in s2)
    s1 = "".join(str(ord(i) - ord('a') + 1) for i in s.lower())
    for _ in range(k):
        s1 = str(dsum(s1))
    return int(s1)

s = "leetcode"
k = 2
print(getLucky(s, k))
