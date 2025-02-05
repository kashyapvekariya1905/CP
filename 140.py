from typing import List
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    def backtrack(start):
        if start == len(s):
            return [[]]
        if start in memo:
            return memo[start]
        rst = []
        for end in range(start+1,len(s)+1):
            word = s[start:end]
            if word in wordDict:
                for sub in backtrack(end):
                    rst.append([word]+sub)
        memo[start] = rst
        return rst
    
    wordDict = set(wordDict)
    memo = {}
    sent = backtrack(0)
    return [" ".join(words) for words in sent]
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(wordBreak(s, wordDict))  # Output: ["cats and dog", "cat sand dog"]

# Example 2
s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
print(wordBreak(s, wordDict))  # Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

# Example 3
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))  # Output: []