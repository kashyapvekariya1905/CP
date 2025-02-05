def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    prev = countAndSay(n-1)
    count = 1
    rst = ""
    for i in range(1, len(prev)+1):
        if i == len(prev) or prev[i]!=prev[i-1]:
            rst += str(count) + prev[i-1]
            count = 1
        else:
            count += 1
    return rst

print(countAndSay(4))
print(countAndSay(1))