s = "(){}[]"
s = list(s)
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        if s[i+1] == ')':
            stack.pop()
    if s[i] == '{':
        stack.append(s[i])
        if s[i+1] == '}':
            stack.pop()
    if s[i] == '[':
        stack.append(s[i])
        if s[i+1] == ']':
            stack.pop()

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # True
print(solution.isValid("()[]{}"))    # True
print(solution.isValid("(]"))        # False
print(solution.isValid("([)]"))      # False
print(solution.isValid("{[]}"))      # True
