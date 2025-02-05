# hamsters = "H..H"
hamsters = ".H.H."
def minimumBuckets(hamsters: str) -> int:
    n = len(hamsters)
    lst = list(hamsters)
    rst = 0
    i = 0
    while i < n:
        if (lst[i] == 'H'):
            if i + 1 < len(lst) and lst[i + 1] == '.':
                lst[i+1] ='f'
                rst+=1
                i+=2
            elif i - 1 >= 0 and lst[i - 1] == '.':
                lst[i-1] = 'f'
                rst+=1
                i+=1
            else:
                return -1
        else:
            i+=1
    print(lst)
    return rst
print(minimumBuckets(hamsters))