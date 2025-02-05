from typing import List
def countBits(n: int) -> List[int]:
    lst = []
    for i in range(n+1):
        lst.append(bin(i)[2:])
        lst[i] = int(lst[i].count('1'))
    return lst

n = 5
print(countBits(n))