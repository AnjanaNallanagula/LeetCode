class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in range(len(s)):
            count = 1
            if (len(stack) != 0 and s[i] == stack[-1][0]):
                char, d = stack.pop()
                count += d
            if (count != k):
                stack.append((s[i], count))
        
        s1 = ""

        for char, d in stack:
            s1 = s1 + (d * char)
        
        return s1