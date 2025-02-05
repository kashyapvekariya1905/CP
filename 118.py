from typing import List

def generate(numRows: int) -> List[int]:
    numRows = numRows+1
    rst = [[1]]
    if numRows <= 0:
        return [1]
    for i in range(1,numRows):
        prev = rst[-1]
        new = [1]
        for j in range(1,len(prev)):
            new.append(prev[j-1]+prev[j])
        new.append(1)
        rst.append(new)
    return rst[-1]

numRows = 3
print(generate(numRows))