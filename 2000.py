word = "abcdefd"
ch = "d"
if ch in word:
    temp = word[:word.index(ch)+1]
    temp2 = word[word.index(ch)+1:]
    temp = temp[::-1]
    out = temp+temp2
