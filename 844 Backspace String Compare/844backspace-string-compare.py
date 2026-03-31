class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        
        for i in s:
            if (i == "#"):
                if (len(stack1) != 0):
                    stack1.pop()
            else:
                stack1.append(i)
        
        for j in t:
            if (j == "#"):
                if (len(stack2) != 0):
                    stack2.pop()
            else:
                stack2.append(j)
        
        if (stack1 == stack2):
            return True
        return False