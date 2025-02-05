class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def generatePalindrome(prefix: int, even: bool) -> int:
            p = prefix
            if not even:
                p = p // 10
            while p:
                prefix = prefix * 10 + p % 10
                p = p // 10
            return prefix

        if len(n) == 1:
            return str(int(n) - 1)

        num = int(n)
        length = len(n)
        
        candidates = [
            10**(length - 1) - 1,
            10**length + 1
        ]
        
        prefix = int(n[:(length + 1) // 2])
        
        for i in range(prefix - 1, prefix + 2):
            candidate = generatePalindrome(i, length % 2 == 0)
            candidates.append(candidate)
        
        result = float('inf')
        for candidate in candidates:
            if candidate != num:
                if abs(candidate - num) < abs(result - num) or \
                   (abs(candidate - num) == abs(result - num) and candidate < result):
                    result = candidate
        
        return str(result)