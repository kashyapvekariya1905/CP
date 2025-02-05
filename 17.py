from typing import List
import itertools
digits = "2"
def letterCombinations(digits: str) -> List[str]:
    
    data = {"2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
    
    if len(digits) == 0:
        return []
    
    rst = []

    lst = list(digits)

    for i in lst:
        if i in data:
            value = data[i]
            rst.append(value)
    com = list(itertools.product(*rst))
    rst = [''.join(i) for i in com]
    return rst

print(letterCombinations(digits))