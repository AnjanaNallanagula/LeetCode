class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {}

        for i in range(len(s)):
            d[s[i]] = i
        
        stack = []
        s1 = set()

        for i in range(len(s)):
            if (s[i] in s1):
                continue
            
            while (len(stack) != 0 and s[i] < stack[-1] and i < d[stack[-1]]):
                char = stack.pop()
                s1.remove(char)
            
            stack.append(s[i])
            s1.add(s[i])
        
        s2 = "".join(stack)

        return s2