from typing import List
def uniqueOccurrences(arr: List[int]) -> bool:
    occ = {}
    lst = []
    for i in arr:
        if i in occ:
            occ[i]+=1
        else:
            occ[i] = 1
    for key,value in occ.items():
        lst.append(value)
    if len(lst) == len(set(lst)):
        return True
    else:
        return False
arr = [1,2]
print(uniqueOccurrences(arr))