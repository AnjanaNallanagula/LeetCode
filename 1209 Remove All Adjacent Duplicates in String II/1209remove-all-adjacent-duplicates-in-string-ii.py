class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in s:
            if (len(stack) != 0 and stack[-1][0] == i):
                stack[-1][1] += 1

                if (stack[-1][1] == k):
                    stack.pop()
            else:
                stack.append([i, 1])
        
        s1 = ""

        for i, d in stack:
            s1 = s1 + (d * i)
        
        return s1