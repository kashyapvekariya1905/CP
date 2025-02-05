s = "bbbab"
freq = {}
ml = 0
st = 0
for i in range(len(s)):
    char = s[i]
    freq[char] = freq.get(char,0)+1

    while len(char)> 2:
        left = s[st]
        freq[left] -=1
        if freq[left] == 0:
            del freq[left]
        st +=1
    ml = int(max(ml, i - st + 1))
print(ml//2)