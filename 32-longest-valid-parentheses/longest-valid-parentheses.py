class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max1 = 0

        for i in range(len(s)):
            if (s[i] == "("):
                stack.append(i)
            else:
                stack.pop()
                
                if (not stack):
                    stack.append(i)
                else:
                    max1 = max(max1, i - stack[-1])
        
        return max1