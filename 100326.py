word = "aaaaaaaaaaaaaabb"
comp = ""
while word:
    pref = 1
    char = word[0]
    for i in range(1, min(9,len(word))):
        if word[i] == char:
            pref +=1
        else:
            break
    
    comp += str(pref)+char
    word = word[pref:] 
print(comp)   