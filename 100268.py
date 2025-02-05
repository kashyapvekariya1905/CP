from typing import List

class Solution:
    def sortSuffixes(self, s):
        def sortKey(i):
            return s[i:]

        n = len(s)
        suffixes = sorted(range(n), key=sortKey)
        return suffixes

    def findLongestCommonSuffix(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        i = 0
        while i < n1 and i < n2 and s1[n1 - 1 - i] == s2[n2 - 1 - i]:
            i += 1
        return i

    def findLongestSuffixIndex(self, s, suffixes, query):
        n = len(s)
        left, right = 0, n - 1
        maxLen, maxIndex = 0, -1

        while left <= right:
            mid = (left + right) // 2
            i = suffixes[mid]
            lcs = self.findLongestCommonSuffix(s[i:], query)
            if lcs > maxLen or (lcs == maxLen and i < maxIndex):
                maxLen, maxIndex = lcs, i
            if s[i:i + lcs] < query:
                left = mid + 1
            else:
                right = mid - 1

        return maxIndex if maxLen > 0 else -1

    def findLongestSuffixes(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        n = len(wordsContainer)
        suffixArrays = [self.sortSuffixes(word) for word in wordsContainer]

        ans = []
        for query in wordsQuery:
            maxIndex = -1
            for i in range(n):
                index = self.findLongestSuffixIndex(wordsContainer[i], suffixArrays[i], query)
                if index != -1:
                    if maxIndex == -1 or (len(wordsContainer[index]) > len(wordsContainer[maxIndex]) if maxIndex >= 0 else True):
                        maxIndex = index
            ans.append(maxIndex)

        return ans

solution = Solution()
wordsContainer = ["abcdefgh", "poiuygh", "ghghgh"]
wordsQuery = ["gh", "acbfgh", "acbfegh"]
print(solution.findLongestSuffixes(wordsContainer, wordsQuery))