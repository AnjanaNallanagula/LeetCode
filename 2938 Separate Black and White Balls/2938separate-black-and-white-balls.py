class Solution:
    def minimumSteps(self, s: str) -> int:
        ls = [0 for i in range(len(s))]

        if (s[0] == "1"):
            ls[0] = 1
        
        for i in range(1, len(s)):
            if (s[i] == "1"):
                ls[i] = ls[i - 1] + 1
            else:
                ls[i] = ls[i - 1]
        
        count = 0

        for i in range(len(ls)):
            if (s[i] == "0"):
                count += ls[i]
        
        return count