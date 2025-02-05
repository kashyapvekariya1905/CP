from typing import List
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]

def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    ordmap = {val:k for k,val in enumerate(arr2)}
    useable = [i for i in arr1 if i in ordmap]
    extra = [i for i in arr1 if i not in ordmap]
    a = sorted(useable,key = lambda x:ordmap[x])
    anot = sorted(extra)
    return a+anot


print(relativeSortArray(arr1,arr2))