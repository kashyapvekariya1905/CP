from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        occ = [(num, freq[num]) for num in nums]
        def srt(item):
            return (item[1], -item[0])
        rst = sorted(occ, key=srt)
        return [num for num, _ in rst]