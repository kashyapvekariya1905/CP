from collections import defaultdict
from typing import List
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    rst = defaultdict(list)
    if len(strs) == 0:
        return []
    if len(strs) == 1:
        return [strs]
    for i in range(len(strs)):
        sortwo = ''.join(sorted(strs[i]))
        rst[sortwo].append(strs[i])
    return list(rst.values())
print(groupAnagrams(strs))